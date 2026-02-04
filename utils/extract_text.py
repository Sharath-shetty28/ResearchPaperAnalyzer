import streamlit as st
import fitz  
def extract_text_from_pdf(file):
    if "file_cache" not in st.session_state:
        st.session_state["file_cache"] = {}

    if file.name not in st.session_state["file_cache"]:
        file_content = file.read()
        with fitz.open(stream=file_content, filetype="pdf") as doc:
            text = ""
            for page in doc:
                text += page.get_text()
            st.session_state["file_cache"][file.name] = text

    return st.session_state["file_cache"][file.name]