import streamlit as st

st.set_page_config(page_title="About | ResearchPaperAnalyzer", page_icon="📚")

st.title("📑 About ResearchPaperAnalyzer")

st.markdown("""
**ResearchPaperAnalyzer** is a Python + Streamlit application designed to make
**research paper analysis fast, simple, and accessible**.

Whether you're a **student, researcher, or professional**, this tool helps you
quickly understand academic papers by extracting key insights, evaluating relevance,
and generating structured reports — all in one place.
""")

st.subheader("🚀 What This App Does")

st.markdown("""
- 📂 **Upload Research Papers**  
  Easily upload one or multiple PDF research papers.

- 📝 **Smart Summarization**  
  Generate **Short, Medium, or Long** summaries depending on your needs.

- 🎯 **Relevance & Alignment Scoring**  
  Enter your topic or domain and receive an **alignment score (0–10)** for each paper.

- 🔖 **Automatic Tag Extraction**  
  Key concepts and relevant keywords are extracted automatically.

- 📄 **Downloadable PDF Report**  
  Export summaries, tags, and scores into a neatly formatted PDF report.

- ⚡ **Fast & Local Execution**  
  Runs locally on your machine for better speed and privacy.
""")

st.subheader("🛠️ Tech Stack")

st.markdown("""
- **Python 3.10+**
- **Streamlit** – User Interface
- **PyPDF2 / pdfminer.six** – PDF text extraction
""")


st.subheader("🎯 Who Is This For?")

st.markdown("""
- Students reviewing multiple papers  
- Researchers validating topic relevance  
- Anyone who wants **faster literature analysis**
""")

st.markdown("---")
st.caption("Built with ❤️ using Python & Streamlit")
