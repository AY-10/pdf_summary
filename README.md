Subject: Technical Assessment Project - Software Engineering Position 
Dear Candidate 
Thank you for your interest in the Software Engineer position at [Company Name]. We've 
reviewed your application and would like to proceed with our technical assessment phase. 
We believe in evaluating candidates through practical, real-world scenarios. Here's your project 
challenge: 
Project: Document Summary Assistant is a n application that takes any document (PDF/Image) 
and generates smart summaries. 
Required Features: 
1. Document Upload: 
● Allow users to upload PDF files and image files (e.g., scanned documents). 
● Support drag-and-drop or file picker interface for easy uploads. 
2. Text Extraction: 
● PDF Parsing: Extract text from PDFs while maintaining formatting. 
● OCR (Optical Character Recognition): For image files (scanned documents), extract text 
using OCR technology (e.g., Tesseract). 
3. Summary Generation: 
● Automatically generate smart summaries of the document content. 
● Provide options for summary length (short, medium, long). 
● Highlight key points and main ideas, ensuring the summary captures essential 
information. 
4. Improvement Suggestions 
9. UI/UX: 
● Simple, intuitive interface for uploading documents and viewing summaries. 
● Mobile-responsive design for use on different devices. 
10. Hosting: 
● Deploy on a reliable hosting service (e.g., Netlify, Vercel, or Heroku) for easy access and 
scalability. 
Technical Requirements: - - - - 
Clean, production-quality code 
Basic error handling 
Loading states for better UX 
Simple documentation explaining your approach 
Technical Freedom: - - - 
Use any frameworks/technologies you're comfortable with 
Free to use AI/ML services (any free tier) 
Collect test data from public sources 
Deliverables: 
1. Working application URL 
2. GitHub repository with source code and README 
3. Brief write-up of your approach (200 words max) 
Timeline: - - 
Project deadline: 1st Sep 2025 
Time investment: Maximum 8 hours 
We'll evaluate based on: - - - - 
Problem-solving approach 
Code quality 
Working functionality 
Documentation 
Next Steps: 
1. Confirm receipt of this email 
2. Submit your GitHub repository link and hosted application URL by the deadline 
3. We'll review and respond within 3 business days 
Questions? Feel free to ask. Good luck! 
Best regards, [Your Name] [Company Name] 

---
## What's included in this repository
- `app.py` — Flask backend (file upload, PDF parsing, OCR fallback, summarization)
- `templates/index.html` — Drag-and-drop frontend
- `static/main.js` — Frontend JS to upload file and display summary
- `requirements.txt`, `Dockerfile`, `Procfile`, `.gitignore`
- `uploads/` folder (gitignored) will store uploaded files locally when running

## Quick start (local)
1. Install system dependency Tesseract OCR:
   - Ubuntu/Debian: `sudo apt-get install tesseract-ocr libtesseract-dev`
   - macOS (Homebrew): `brew install tesseract`
2. Create and activate a virtual environment, then install Python deps:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
3. Run the app:
```bash
python app.py
```
4. Open http://127.0.0.1:5000 in your browser.

## 200-word approach (deliverable)
This application ingests PDFs and images, extracts their textual contents, and produces short/medium/long summaries. For PDFs we prefer PyMuPDF because it extracts structured text without rasterizing pages, preserving reading order; for scanned PDFs or images we run Tesseract OCR using pytesseract after pre-processing with Pillow. Extracted text is chunked when large and fed into a transformer-based summarization pipeline (Hugging Face) with configurable max/min lengths for short/medium/long outputs. The UI is a single-page drag-and-drop interface that calls the Flask backend and displays summaries and highlighted key sentences. Error handling covers unsupported files, OCR fallback, and empty results; loading indicators on the frontend improve UX. The repo includes a Dockerfile and Procfile for easy deployment to Heroku or container platforms. For production, consider using a hosted LLM (OpenAI) to reduce model size and latency, chunking/streaming for very large documents, and authentication/rate-limiting for multi-user scenarios.
