import streamlit as st
from core.chunk_text import chunk_text, filter_chunks
from core.extract_text import extract_text_from_pdf
from prompts.ratings import ratings

def render_relevance_section(uploaded_files, client, model, temperature):
    with st.expander("🎯 Topic Relevance Scanner & Tagging"):
        topic = st.text_input("📝 Enter a topic to check relevance:")

        if not topic:
            return

        if "relevance_results" not in st.session_state:
            st.session_state["relevance_results"] = {}

        for file in uploaded_files:
            st.subheader(f"📘 {file.name}")

            if file.name not in st.session_state["relevance_results"]:
                st.session_state["relevance_results"][file.name] = ""

            if st.button("Check Relevance", key=f"rel_{file.name}"):
                with st.spinner("Checking relevance..."):
                    text = extract_text_from_pdf(file)
                    chunks = chunk_text(text)
                    relevant_chunks = filter_chunks(chunks, topic)
                    context = "\n\n---\n\n".join(relevant_chunks)

                    prompt = ratings(context, topic)
                    response = client.chat.completions.create(
                        model=model,
                        messages=[{"role": "user", "content": prompt}],
                        temperature=temperature
                    )

                    st.session_state["relevance_results"][file.name] = (
                        response.choices[0].message.content.strip()
                    )

            if st.session_state["relevance_results"][file.name]:
                st.text_area(
                    "🎯 Relevance Result",
                    st.session_state["relevance_results"][file.name],
                    height=200,
                    key=f"out_{file.name}"
                )
