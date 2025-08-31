from flask import Flask, request, render_template, jsonify
import os
from werkzeug.utils import secure_filename
from pathlib import Path

UPLOAD_FOLDER = "uploads"
ALLOWED = {"pdf", "png", "jpg", "jpeg", "tiff", "tif"}

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app = Flask(__name__, static_folder="static", template_folder="templates")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 80 * 1024 * 1024  # 80MB

# Optional imports (may not be installed in test env)
try:
    import fitz  # pymupdf
except Exception:
    fitz = None

try:
    from PIL import Image
    import pytesseract
except Exception:
    Image = None
    pytesseract = None

# summarization (transformers)
try:
    from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM
    summarizer = pipeline("summarization")
except Exception:
    summarizer = None

def allowed_file(filename):
    return "." in filename and filename.rsplit(".",1)[1].lower() in ALLOWED

def extract_text_from_pdf(path):
    if fitz is None:
        return ""
    try:
        doc = fitz.open(path)
        texts = []
        for page in doc:
            texts.append(page.get_text("text"))
        return "\n".join(texts)
    except Exception as e:
        return ""

def ocr_image(path):
    if Image is None or pytesseract is None:
        return ""
    try:
        img = Image.open(path)
        text = pytesseract.image_to_string(img)
        return text
    except Exception as e:
        return ""

def summarize_text(text, length='medium'):
    if not summarizer:
        return "Summarizer not available. Please install the transformers package."
    mapping = {'short': (20,60), 'medium': (60,180), 'long': (180,400)}
    min_len, max_len = mapping.get(length, mapping['medium'])
    # Trim extremely long texts for local summarizers
    words = text.split()
    if len(words) > 1200:
        text = " ".join(words[:1200])
    try:
        out = summarizer(text, max_length=max_len, min_length=min_len, do_sample=False)
        if isinstance(out, list) and len(out)>0:
            return out[0].get('summary_text','')
        return str(out)
    except Exception as e:
        return f"Summarization error: {str(e)}"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/upload", methods=["POST"])
def upload():
    if 'file' not in request.files:
        return jsonify({'error':'no file part'}), 400
    f = request.files['file']
    if f.filename == "":
        return jsonify({'error':'no file selected'}), 400
    if f and allowed_file(f.filename):
        filename = secure_filename(f.filename)
        save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        f.save(save_path)
        ext = filename.rsplit('.',1)[1].lower()
        text = ""
        if ext == 'pdf':
            text = extract_text_from_pdf(save_path)
            if not text.strip():
                # If PDF text empty, try converting first page to image for OCR (simple fallback)
                try:
                    if fitz is not None:
                        doc = fitz.open(save_path)
                        page = doc.load_page(0)
                        pix = page.get_pixmap(dpi=200)
                        img_path = save_path + "_page0.png"
                        pix.save(img_path)
                        text = ocr_image(img_path)
                        try:
                            os.remove(img_path)
                        except:
                            pass
                except Exception:
                    pass
        else:
            text = ocr_image(save_path)
        if not text or not text.strip():
            return jsonify({'error':'no text found via parsing/OCR'}), 422
        length = request.form.get('length','medium')
        summary = summarize_text(text, length=length)
        return jsonify({'summary': summary, 'text_snippet': text[:2000]})
    else:
        return jsonify({'error':'file type not allowed'}), 415

if __name__ == "__main__":
    # Bind to all interfaces so container/host can access it
    app.run(host="0.0.0.0", port=5000, debug=True)
