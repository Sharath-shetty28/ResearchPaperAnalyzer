import streamlit as st
from core.chunk_text import chunk_text
from core.extract_text import extract_text_from_pdf
from prompts.refine_method import (
    build_initial_summary_prompt,
    build_refine_summary_prompt,
)

def render_summarize_section(uploaded_files, client, model, temperature):
    if "summaries" not in st.session_state:
        st.session_state["summaries"] = {}

    if "pdf_texts" not in st.session_state:
        st.session_state["pdf_texts"] = {}

    with st.expander("📌 Summarize PDFs", expanded=True):
        for file in uploaded_files:
            st.subheader(f"📘 {file.name}")

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
                with st.spinner("Generating refined summary with AI..."):
                    chunks = chunk_text(text)[:8]
                    summary = ""

                    for i, chunk in enumerate(chunks):
                        if i == 0:
                            prompt = build_initial_summary_prompt(chunk, summary_length)
                        else:
                            prompt = build_refine_summary_prompt(summary, chunk, summary_length)

                        response = client.chat.completions.create(
                            model=model,
                            messages=[{"role": "user", "content": prompt}],
                            temperature=temperature
                        )
                        summary = response.choices[0].message.content.strip()

                    st.session_state["summaries"][file.name] = summary

            if file.name in st.session_state["summaries"]:
                st.markdown(st.session_state["summaries"][file.name])
