# 📑 ResearchPaperAnalyzer

ResearchPaperAnalyzer is a **Python + Streamlit** application that helps users analyze research papers with ease.  
It allows you to **upload PDFs**, generate **summaries** (Short / Medium / Long), extract **relevant tags**, check **alignment scores** (0–10) against your chosen topic/domain, and finally **download a PDF report**.


## Live demo :
```bash
nexaread.streamlit.app
```
---

## 🚀 Features
- 📂 **Upload PDF**: Drag-and-drop one or multiple papers.  
- 📝 **Summarization**: Generate **Short, Medium, or Long** summaries.  
- 🎯 **Relevance Scoring**: Enter your topic/domain → get an **alignment score (0–10)** for each paper.  
- 🔖 **Tag Extraction**: Auto-generated keywords and relevant topics.  
- 📄 **PDF Report**: Download a compiled report with summaries, tags, and scores.  
- ⚡ **Fast & Local**: Runs entirely on your machine.  

---

## 🛠️ Tech Stack
- **Python 3.10+**  
- **Streamlit** (UI framework)  
- **PyPDF2 / pdfminer.six** (PDF text extraction)  

---

## 📦 Installation

```bash
# Clone repository
git clone https://github.com/<your-username>/ResearchPaperAnalyzer.git
cd ResearchPaperAnalyzer

# Create virtual environment
python -m venv .venv
# Activate (Windows)
.venv\Scripts\activate
# Activate (macOS/Linux)
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

```


▶️ Usage

Run the app:
```bash

streamlit run app.py

```

Open in your browser:
```bash
http://localhost:8501
```


## Steps:
- Enter your target topic/domain.
- Upload one or more PDFs.
- Select summary type (Short, Medium, Long).
- View summaries, tags, and alignment scores.
- Export results as a downloadable PDF report.




## 📊 Example Output

- Summary (short/medium/long)
- Tags: e.g., ["Neural Networks", "Graph Models", "Recommendation"]
- Relevance Score: 8.5 / 10
- Generated Report: Downloadable .pdf



## 🤝 Contributing

Pull requests are welcome! Please open an issue for major changes or feature requests.
