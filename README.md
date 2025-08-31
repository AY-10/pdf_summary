# 📄 Document Summary Assistant

An AI-powered application that extracts and summarizes content from documents (PDFs, Images) and generates smart summaries.  
Built as part of a **Technical Assessment Project - Software Engineering Position**.

🔗 **Live Demo:** [doc-sum-td55.vercel.app](https://doc-sum-td55.vercel.app)

---

## 🚀 Features

1. **Document Upload**
   - Drag-and-drop or file picker for uploads
   - Supports PDF files and image formats (JPG, PNG, TIFF, BMP, etc.)

2. **Text Extraction**
   - **PDF Parsing** with PyMuPDF for structured text extraction
   - **OCR Processing** using pytesseract for scanned images and documents

3. **AI-powered Summarization**
   - Generates **short, medium, and long summaries**
   - Extracts **key points and main ideas**
   - Highlights **essential information**

4. **UI/UX**
   - Clean, intuitive interface with drag-and-drop functionality
   - Mobile-responsive design
   - Loading states for better user experience

5. **Hosting**
   - Deployed on **Vercel** for easy access and scalability

---

## 🛠️ Tech Stack

- **Backend:** Flask (Python)
- **PDF Processing:** PyMuPDF (fitz)
- **OCR:** pytesseract + Tesseract OCR
- **Image Processing:** Pillow (PIL)
- **Summarization:** Hugging Face Transformers
- **Frontend:** HTML5, CSS3, JavaScript
- **Deployment:** Vercel
- **Containerization:** Docker support included

---

## 📂 Project Structure

```
pdf_summary/
├── app.py                 # Flask backend (main application)
├── templates/
│   └── index.html        # Frontend interface
├── static/
│   └── main.js           # Frontend JavaScript
├── requirements.txt      # Python dependencies
├── Dockerfile           # Docker configuration
├── Procfile            # Heroku deployment config
├── uploads/            # Local file storage (gitignored)
└── README.md
```

---

## ⚡ Quick Start (Local)

### Prerequisites

**Install Tesseract OCR:**
```bash
# Ubuntu/Debian
sudo apt-get install tesseract-ocr libtesseract-dev

# macOS (Homebrew)
brew install tesseract

# Windows
# Download from: https://github.com/UB-Mannheim/tesseract/wiki
```

### Setup

```bash
# Clone repository
git clone https://github.com/AY-10/pdf_summary.git
cd pdf_summary

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run application
python app.py
```

Open http://127.0.0.1:5000 in your browser.

---

## 🐳 Docker Setup

```bash
# Build Docker image
docker build -t document-summary-assistant .

# Run container
docker run -p 5000:5000 document-summary-assistant
```

---

## 📦 Deployment

### Vercel Deployment
- **Frontend:** Deployed to Vercel
- **Backend:** Serverless functions or separate API deployment

### Alternative Platforms
- **Heroku:** Use included `Procfile`
- **Docker:** Container-ready with `Dockerfile`
- **Railway/Render:** Compatible with Python deployments

---

## 🔧 API Endpoints

### Upload and Summarize
```http
POST /summarize
Content-Type: multipart/form-data

Parameters:
- file: Document file (PDF/Image)
- summary_length: "short" | "medium" | "long"

Response:
{
  "summary": "Generated summary text",
  "key_points": ["point1", "point2", "point3"],
  "word_count": 250,
  "processing_time": 3.2
}
```

---

## 💡 How It Works

1. **Upload Document** - Drag and drop or select PDF/image files
2. **Text Extraction** - PyMuPDF for PDFs, Tesseract OCR for images
3. **Content Analysis** - Preprocessing and text cleaning
4. **AI Summarization** - Hugging Face transformers generate summaries
5. **Display Results** - Summary and key points rendered in clean UI

---

## 🧪 Testing

### Test with Sample Documents
- Upload various PDF types (text-based, scanned)
- Test image formats (JPG, PNG, TIFF)
- Verify different summary lengths
- Check mobile responsiveness

---

## ✨ Deliverables

- ✅ **Working Application URL:** [doc-sum-td55.vercel.app](https://doc-sum-td55.vercel.app)
- ✅ **GitHub Repository:** [github.com/AY-10/pdf_summary](https://github.com/AY-10/pdf_summary)
- ✅ **Technical Write-up:** 200-word approach document

---

## 📝 Technical Approach (200 Words)

This application ingests PDFs and images, extracts their textual contents, and produces short/medium/long summaries. For PDFs we use PyMuPDF because it extracts structured text without rasterizing pages, preserving reading order; for scanned PDFs or images we run Tesseract OCR using pytesseract after pre-processing with Pillow. 

Extracted text is chunked when large and fed into a transformer-based summarization pipeline (Hugging Face) with configurable max/min lengths for short/medium/long outputs. The UI is a single-page drag-and-drop interface that calls the Flask backend and displays summaries and highlighted key sentences. 

Error handling covers unsupported files, OCR fallback, and empty results; loading indicators on the frontend improve UX. The repo includes a Dockerfile and Procfile for easy deployment to Heroku or container platforms. 

For production, consider using a hosted LLM (OpenAI) to reduce model size and latency, chunking/streaming for very large documents, and authentication/rate-limiting for multi-user scenarios.

---

## 👨‍💻 Author

- **Name:** Anurag Yadav
- **Roll Number:** 2201641530040
- **Branch:** CSE AIML
- **Assignment:** Document Summary Assistant - Assignment 3
- **Email:** anuragyadavatwork@gmail.com

---


