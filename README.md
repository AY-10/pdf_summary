# 📄 AI Document Summary Assistant

An AI-powered application that extracts, understands, and summarizes content from documents (PDFs & Images), helping students and professionals quickly grasp key information without reading entire files.

🔗 **Live Demo:** https://doc-sum-td55.vercel.app  
📁 **GitHub:** https://github.com/AY-10/pdf_summary  

---

## 💡 Why I Built This

Students and professionals often spend significant time reading long documents. I built this tool to reduce that friction by allowing users to upload documents and instantly get concise summaries and key insights, improving productivity and learning efficiency.

---

## 🚀 Features

- 📄 **PDF & Image Upload** — Supports PDFs, JPG, PNG, TIFF  
- 🧠 **Smart Text Extraction** — PyMuPDF for PDFs, Tesseract OCR for scanned docs  
- ✨ **AI Summarization** — Generates short, medium, and long summaries  
- 🔑 **Key Points Extraction** — Highlights most important concepts  
- 📱 **Clean UI** — Responsive and user-friendly interface  
- ⚡ **Fast Processing** — Optimized for quick responses  
- 🐳 **Dockerized** — Easy deployment anywhere  

---

## 🛠️ Tech Stack

- **Backend:** Flask (Python)  
- **AI/NLP:** HuggingFace Transformers  
- **OCR:** pytesseract + Tesseract  
- **PDF Processing:** PyMuPDF (fitz)  
- **Image Processing:** Pillow (PIL)  
- **Frontend:** HTML, CSS, JavaScript  
- **Deployment:** Vercel  
- **Containerization:** Docker  

---

## 📂 Project Structure

```
pdf_summary/
├── app.py                 # Flask backend
├── templates/
│   └── index.html         # Frontend UI
├── static/
│   └── main.js            # Frontend logic
├── requirements.txt       # Dependencies
├── Dockerfile             # Docker config
├── Procfile               # Deployment config
└── README.md
```

---

## ⚡ Run Locally

### 1. Install Tesseract OCR

```
# Ubuntu/Debian
sudo apt-get install tesseract-ocr libtesseract-dev

# macOS
brew install tesseract

# Windows
Download from:
https://github.com/UB-Mannheim/tesseract/wiki
```

---

### 2. Setup & Run

```
git clone https://github.com/AY-10/pdf_summary.git
cd pdf_summary

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
python app.py
```

Visit: http://127.0.0.1:5000

---

## 🐳 Docker Setup

```
docker build -t ai-document-summary .
docker run -p 5000:5000 ai-document-summary
```

---

## 🔧 API

### POST `/summarize`

**Request:**
- Content-Type: multipart/form-data  
- Parameters:
  - `file` → PDF/Image  
  - `summary_length` → short | medium | long  

**Response:**
```json
{
  "summary": "...",
  "key_points": ["...", "..."],
  "word_count": 250,
  "processing_time": 3.2
}
```

---

## ⚙️ How It Works

1. User uploads a document (PDF/Image)  
2. Text is extracted using:
   - PyMuPDF (for PDFs)
   - Tesseract OCR (for images)  
3. Extracted text is processed and chunked  
4. HuggingFace model generates summary + key insights  
5. Results are displayed instantly in UI  

---

## 🧠 Product Thinking

- Reduces **cognitive load** for users  
- Converts passive reading → **active understanding**  
- Focused on **speed + usability** rather than complexity  
- Designed as a foundation for AI-powered learning tools  

---

## 🔮 Future Improvements

- Integrate OpenAI / Claude for better summaries  
- Generate quizzes from documents  
- Add “Explain like I’m 10” feature  
- Chat with document (RAG-based Q&A)  
- User dashboard with history  

---

## 👨‍💻 Author

**Anurag Yadav**  
📧 anuragyadavatwork@gmail.com  
🔗 https://linkedin.com/in/ay10  
💻 https://github.com/AY-10  

---

## ⭐ If you like this project

Give it a star ⭐ — it helps and motivates further improvements!
