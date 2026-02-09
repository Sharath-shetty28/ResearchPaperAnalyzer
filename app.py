import streamlit as st
from groq import Groq
from dotenv import load_dotenv
from config.export_utils import PDFReport
import os
from ui.sidebar import render_sidebar
from core.extract_text import extract_text_from_pdf
from prompts.summarize import build_summary_prompt
from prompts.ratings import ratings
from openai import OpenAI

# ===== env setup ==========

load_dotenv()


# Get key from Streamlit Secrets (cloud) or env (local)
api_key = st.secrets.get("GROQ_API_KEY") or os.getenv("GROQ_API_KEY")

if not api_key:
    st.error("GROQ_API_KEY not found. Please set it in Streamlit Secrets.")
    st.stop()

client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1"
)

# ---------- Streamlit UI ----------
st.set_page_config(
    page_title="RAG PDF Chat System",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ---------- MENU BAR  ----------
model, temperature = render_sidebar()

# 🔧 Common footer/debug
st.sidebar.divider()
st.sidebar.write("### Current Config:")
st.sidebar.write("Model:", model)
st.sidebar.write("Temp:", temperature)

st.title("📑 ResearchPaperAnalyzer")


# ---------- Upload PDFs ----------
st.subheader("📤 Upload PDF Files")
uploaded_files = st.file_uploader('',type=["pdf"], accept_multiple_files=True, key="uploaded_files")

# ---------- Main Sections ----------
if uploaded_files:

    if "summaries" not in st.session_state:
        st.session_state["summaries"] = {}

    if "pdf_texts" not in st.session_state:
        st.session_state["pdf_texts"] = {}

    with st.expander("📌 Summarize PDFs", expanded=True):
        for file in uploaded_files:
            st.subheader(f"📘 {file.name}")

            # Extract once and store
            if file.name not in st.session_state["pdf_texts"]:
                with st.spinner("Extracting text..."):
                    st.session_state["pdf_texts"][file.name] = extract_text_from_pdf(file)

            text = st.session_state["pdf_texts"][file.name]

            if not text.strip():
                st.warning("No readable text found in this PDF.")
                continue

            summary_length = st.selectbox(
                f"Choose summary length for {file.name}",
                ["Short", "Medium", "Detailed"],
                index=1,
                key=f"length_{file.name}"
            )

            if st.button("Summarize", key=f"btn_{file.name}"):
                with st.spinner("Generating summary with AI..."):
                    prompt = build_summary_prompt(text, summary_length)

                    response = client.chat.completions.create(
                        model=model,
                        messages=[{"role": "user", "content": prompt}],
                        temperature=temperature
                    )

                    st.session_state["summaries"][file.name] = (
                        response.choices[0].message.content
                    ).strip()

            if file.name in st.session_state["summaries"]:
                st.markdown(st.session_state["summaries"][file.name])

    # --- Section 2: Topic Relevance & Tagging ---
    with st.expander("🎯 Topic Relevance Scanner & Tagging"):
        topic = st.text_input("📝 Enter a topic to check relevance:")
        if topic:
            st.session_state["topic_query"] = topic

        if "relevance_results" not in st.session_state:
            st.session_state["relevance_results"] = {}

        for file in uploaded_files:
            st.subheader(f"📘 {file.name}")
            with st.spinner("Extracting text..."):
                text = extract_text_from_pdf(file)

        # Initialize this file's result if not already stored
            if file.name not in st.session_state["relevance_results"]:
                st.session_state["relevance_results"][file.name] = ""

            if st.button("Check Relevance"):
                with st.spinner("Checking relevance..."):
                    prompt2 = ratings(text, topic)
                    response = client.chat.completions.create(
                        model=model,
                        messages=[{"role": "user", "content": prompt2}],
                        temperature=temperature
                    )
                    st.session_state["relevance_results"][file.name] = response.choices[0].message.content.strip()

        # Always display this PDF's relevance result if it exists
            if st.session_state["relevance_results"][file.name]:
                st.text_area(
                    "🎯 Relevance Result",
                    st.session_state["relevance_results"][file.name],
                    height=200, key=f"relevance_{file.name}" 
                )


    # # --- Section 3: Export Final Report ---
    with st.expander("📄 Export Final Report", expanded=True):

    # make sure we have one report object in session state
        if "report" not in st.session_state:
            st.session_state.report = PDFReport()

        if st.button("📥 Generate PDF Report"):
            with st.spinner("Compiling report..."):
                # reset first so we don't append old content
                st.session_state.report.clear()

                # Add summaries
                for fname, summary in st.session_state["summaries"].items():
                    relevance = st.session_state["relevance_results"].get(fname, "")
                    st.session_state.report.add_pdf_summary(fname, summary, relevance)

                file_path = st.session_state.report.save("Final_Report.pdf")
                with open(file_path, "rb") as f:
                    st.download_button(
                        "⬇️ Download Final Report",
                        f,
                        "Final_Report.pdf",
                        "application/pdf"
                    )

    if st.button("🗑️ Clear All"):
        st.session_state["summaries"] = {}
        st.session_state["relevance_results"] = {}
        st.success("All files and results cleared!")
        st.rerun()    


            

