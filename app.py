import streamlit as st
from groq import Groq
from dotenv import load_dotenv
from config.export_utils import PDFReport
import os
from ui.sidebar import render_sidebar
from ui.relevance import render_relevance_section
from ui.summarize import render_summarize_section
from ui.pdf_report import render_export_section
from openai import OpenAI

# ===== env setup ==========

# load_dotenv()
# client = Groq(api_key=os.getenv("GROQ_API_KEY"))

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

    # # --- Section 1: Summarize ---
    render_summarize_section(uploaded_files, client, model, temperature)

    # # --- Section 2: Relevance ---
    render_relevance_section(uploaded_files, client, model, temperature)

    # # --- Section 3: Export Final Report ---
    render_export_section()
    