# StudyZoneCodex

An AI-powered study platform that transforms any PDF into summaries, quizzes, flashcards and an interactive chat.

## Features

- **Summary** — AI reads your PDF and extracts key concepts
- **Quiz** — Auto generates MCQ, True/False and Short Answer questions
- **Chat** — Ask your AI sensei anything about the uploaded document
- **File Manager** — Upload, save and delete your study PDFs

## Tech Stack

- **Backend** — Python, Flask
- **AI** — Groq API (LLaMA3)
- **PDF Parsing** — pdfplumber


## Setup

1. Clone the repository
```bash
   git clone https://github.com/yourusername/studyzonecodex.git
   cd studyzonecodex
```

2. Install dependencies
```bash
   pip install -r requirements.txt
```

3. Create `.env` file and add your Groq API key
```
   GROQ_API_KEY=your_key_here
```

4. Create uploads folder
```bash
   mkdir uploads
```

5. Run the app
```bash
   python app.py
```

6. Open `http://127.0.0.1:5000` in your browser

## Project Structure
```
studyzonecodex/
    app.py              — Flask routes
    utils/
        pdf_parser.py   — Extract text from PDF
        ai_helper.py    — Groq AI calls
        file_manager.py — File operations
    templates/          — HTML pages
    static/             — CSS and JS files
    uploads/            — Saved PDFs
```

## Author

Made by Monu — github.com/venux09
website is live :-https://studyzonecodex-3.onrender.com/
using render and meeting requirement it is live succesfully
