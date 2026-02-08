import streamlit as st

from core.extract_text import extract_text_from_pdf
from core.chunking import chunk_text
from core.vector_store import add_pdf_chunks
from config.settings import CHUNK_SIZE, CHUNK_OVERLAP


def render_upload_ui(uploaded_files):

    if "indexed_pdfs" not in st.session_state:
        st.session_state["indexed_pdfs"] = set()

    if not uploaded_files:
        return []

    for file in uploaded_files:
        if file.name in st.session_state["indexed_pdfs"]:
            st.success(f"✅ {file.name} already indexed")
            continue

        with st.spinner(f"Processing {file.name}..."):
            # 1. Extract text
            text = extract_text_from_pdf(file)

            # 2. Chunk text
            chunks = chunk_text(
                text,
                chunk_size=CHUNK_SIZE,
                overlap=CHUNK_OVERLAP
            )

            # 3. Store in ChromaDB
            add_pdf_chunks(file.name, chunks)

            # 4. Mark as indexed
            st.session_state["indexed_pdfs"].add(file.name)

        st.success(f"📚 {file.name} indexed successfully")

    return uploaded_files