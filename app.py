import streamlit as st
from groq import Groq
from dotenv import load_dotenv
from groq import Groq
import os
import fitz  
from utils.sidebar import render_sidebar
from utils.extract_text import extract_text_from_pdf
from prompts.summarize import summarize_prompt
from export_utils import PDFReport

# ===== env setup ==========

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


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

# ---------- Upload PDFs ----------
uploaded_files = st.file_uploader("📤 Upload one or more PDF files", type=["pdf"], accept_multiple_files=True,key="uploaded_files" )

# ---------- Main Sections ----------
if uploaded_files:

    # --- Section 1: Summarize PDFs ---
    if "summaries" not in st.session_state:
        st.session_state["summaries"] = {}

    with st.expander("📌 Summarize PDFs", expanded=True):
        for file in uploaded_files:
            st.subheader(f"📘 {file.name}")

            with st.spinner("Extracting text..."):
                text = extract_text_from_pdf(file)

        # Summary length selector
            summary_length = st.selectbox(
                f"Choose summary length for {file.name}",
                ["Short", "Medium", "Detailed"],
                index=1,
                key=f"length_{file.name}"
            )

            if st.button(f"Summarize", key=f"btn_{file.name}"):
                with st.spinner("Generating summary with AI..."):
                    summary = summarize_prompt(text, length=summary_length)
                    st.session_state["summaries"][file.name] = summary

            # Show summary if it exists
            if file.name in st.session_state["summaries"]:
                st.markdown(st.session_state["summaries"][file.name])

    # # --- Section 2: Topic Relevance & Tagging ---
    # with st.expander("🎯 Topic Relevance Scanner & Tagging"):
    #     topic = st.text_input("📝 Enter a topic to check relevance:")
    #     if topic:
    #         st.session_state["topic_query"] = topic

    #     if "relevance_results" not in st.session_state:
    #         st.session_state["relevance_results"] = {}

    #     for file in uploaded_files:
    #         st.subheader(f"📘 {file.name}")
    #         with st.spinner("Extracting text..."):
    #             text = extract_text_from_pdf(file)

    #     # Initialize this file's result if not already stored
    #         if file.name not in st.session_state["relevance_results"]:
    #             st.session_state["relevance_results"][file.name] = ""

    #         if st.button(f"Check Relevance - {file.name}"):
    #             with st.spinner("Checking relevance..."):
    #                 relevance = check_relevance_with_gemini(text, topic)
    #                 st.session_state["relevance_results"][file.name] = relevance

    #     # Always display this PDF's relevance result if it exists
    #         if st.session_state["relevance_results"][file.name]:
    #             st.text_area(
    #                 "🎯 Relevance Result",
    #                 st.session_state["relevance_results"][file.name],
    #                 height=200, key=f"relevance_{file.name}" 
    #             )

    # # --- Section 3: Export Final Report ---
    # with st.expander("📄 Export Final Report", expanded=True):

    # # make sure we have one report object in session state
    #     if "report" not in st.session_state:
    #         st.session_state.report = PDFReport()

    #     if st.button("📥 Generate PDF Report"):
    #         with st.spinner("Compiling report..."):
    #             # reset first so we don't append old content
    #             st.session_state.report.clear()

    #             # Add summaries
    #             for fname, summary in st.session_state["summaries"].items():
    #                 relevance = st.session_state["relevance_results"].get(fname, "")
    #                 st.session_state.report.add_pdf_summary(fname, summary, relevance=relevance)

    #             file_path = st.session_state.report.save("Final_Report.pdf")
    #             with open(file_path, "rb") as f:
    #                 st.download_button(
    #                     "⬇️ Download Final Report",
    #                     f,
    #                     "Final_Report.pdf",
    #                     "application/pdf"
    #                 )

    # if st.button("🗑️ Clear All"):
    #     st.session_state["summaries"] = {}
    #     st.session_state["relevance_results"] = {}
    #     st.success("All files and results cleared!")
    #     st.rerun()    


            

