# 📑 ResearchPaperAnalyzer

ResearchPaperAnalyzer is a **Streamlit + Groq API** powered application that helps users **analyze academic research papers efficiently**.

It allows you to upload one or more PDFs, generate **structured summaries**, evaluate **topic relevance**, extract **key tags**, and export everything into a **downloadable PDF report** — all through an intuitive web interface.

---

## 🚀 Features

- 📂 **Upload PDF**  
  Drag-and-drop one or multiple research papers.

- 📝 **Summarization**  
  Generate **Short, Medium, or Detailed** summaries using structured prompts.

- 🎯 **Relevance Scoring**  
  Enter a topic or domain and receive an **alignment score (0–10)** for each paper.

- 🔖 **Tag Extraction**  
  Automatically extract important keywords and research themes.

- 📄 **PDF Report Export**  
  Download a compiled report containing summaries, relevance scores, and tags.

- ⚡ **Fast & Local Execution**  
  PDF processing runs locally; only AI inference uses the Groq API.

---

## 🧠 How It Works

1. Upload one or more PDF research papers
2. Text is extracted and cached locally
3. Documents are chunked for long-context safety
4. Groq LLM is used with **structured prompts** to:
   - Generate summaries (Refine method)
   - Score relevance to a given topic
   - Extract key tags
5. Results are compiled into a final PDF report

---

## 📁 Project Structure

```bash

ResearchPaperAnalyzer/
├─ .devcontainer/
│ └─ devcontainer.json
├─ config/
│ ├─ **pycache**/
│ │ ├─ **init**.cpython-313.pyc
│ │ ├─ export_utils.cpython-313.pyc
│ │ └─ setting.cpython-313.pyc
│ ├─ **init**.py
│ ├─ export_utils.py
│ └─ setting.py
├─ core/
│ ├─ **pycache**/
│ │ ├─ **init**.cpython-313.pyc
│ │ ├─ chunk_text.cpython-313.pyc
│ │ └─ extract_text.cpython-313.pyc
│ ├─ **init**.py
│ ├─ chunk_text.py
│ └─ extract_text.py
├─ pages/
│ ├─ 1_About.py
│ └─ 2_Contact_Me.py
├─ prompts/
│ ├─ **pycache**/
│ │ ├─ length_instruction.cpython-313.pyc
│ │ ├─ ratings.cpython-313.pyc
│ │ ├─ refine_method.cpython-313.pyc
│ │ └─ summarize.cpython-313.pyc
│ ├─ length_instruction.py
│ ├─ ratings.py
│ └─ refine_method.py
├─ ui/
│ ├─ **pycache**/
│ │ ├─ **init**.cpython-313.pyc
│ │ ├─ pdf_report.cpython-313.pyc
│ │ ├─ relevance.cpython-313.pyc
│ │ ├─ sidebar.cpython-313.pyc
│ │ └─ summarize.cpython-313.pyc
│ ├─ **init**.py
│ ├─ pdf_report.py
│ ├─ relevance.py
│ ├─ sidebar.py
│ └─ summarize.py
├─ .env
├─ .gitignore
├─ app.py
├─ README.md
└─ requirements.txt

```

## 🛠️ Tech Stack

- **Python 3.10+**
- **Streamlit** – Web UI
- **Groq API** – LLM inference
- **PyMuPDF / pdfminer.six** – PDF text extraction
- **fpdf2** – PDF report generation

---

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/<your-username>/ResearchPaperAnalyzer.git
cd ResearchPaperAnalyzer

# Create and activate virtual environment
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## 🔑 Environment Setup

Create a .env file for local development:

```bash
GROQ_API_KEY = "your_groq_api_key_here"
```

## ▶️ Usage

Run the app locally:

```bash
streamlit run app.py
```

Open in your browser:

```bash
http://localhost:8501
```

## 📌 Notes

1. Designed for researchers, students, and engineers
2. Uses Refine-based summarization for long documents
3. Optimized to reduce hallucinations and token usage
4. Built with scalability and clean architecture in mind

## 📊 Example Output

- Summary (short/medium/long)
- Tags: e.g., ["Neural Networks", "Graph Models", "Recommendation"]
- Relevance Score: 8.5 / 10
- Generated Report: Downloadable .pdf

## 🤝 Contributing

- Contributions are welcome!
- Open an issue for feature requests or bugs
- Submit a pull request for improvements
- Keep changes modular and documented
