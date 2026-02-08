import streamlit as st
from core.vector_store import retrieve_chunks
from core.relevance import get_relevance

def render_relevance_ui(uploaded_files):
    topic = st.text_input("📝 Enter topic")

    if not topic:
        return

    for file in uploaded_files:
        st.subheader(file.name)

        if st.button("Check Relevance", key=file.name):
            chunks = retrieve_chunks(topic)
            result = get_relevance(topic, chunks)

            st.text_area("Result", result, height=180)