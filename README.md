---

## ⚡ Run Locally

### 1. Install Tesseract OCR
```bash
# Ubuntu/Debian
sudo apt-get install tesseract-ocr libtesseract-dev

# macOS
brew install tesseract

# Windows — download from:
# https://github.com/UB-Mannheim/tesseract/wiki
```

### 2. Setup & Run
```bash
git clone https://github.com/AY-10/pdf_summary.git
cd pdf_summary

python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

pip install -r requirements.txt
python app.py
```

Visit http://127.0.0.1:5000

---

## 🐳 Docker
```bash
docker build -t document-summary-assistant .
docker run -p 5000:5000 document-summary-assistant
```

---

## 🔧 API
```http
POST /summarize
Content-Type: multipart/form-data

Parameters:
  file           → PDF or image file
  summary_length → "short" | "medium" | "long"

Response:
{
  "summary": "...",
  "key_points": ["...", "..."],
  "word_count": 250,
  "processing_time": 3.2
}
```

---

## 💡 How It Works

1. User uploads PDF or image
2. PyMuPDF extracts text from PDFs / Tesseract OCR handles images
3. Text is chunked and passed to HuggingFace summarization pipeline
4. Summary and key points returned and displayed instantly

---

## 🔮 Future Improvements

- Switch to OpenAI/Claude API for faster, higher quality summaries
- Add quiz generation from uploaded content
- User accounts with document history
- Streaming responses for large documents
- Chat with your document (RAG-based Q&A)

---

## 👨‍💻 Author

**Anurag Yadav**
anuragyadavatwork@gmail.com | [LinkedIn](https://linkedin.com/in/ay10) | 
[GitHub](https://github.com/AY-10)
