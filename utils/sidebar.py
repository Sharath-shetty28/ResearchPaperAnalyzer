import streamlit as st

def render_sidebar():

    # -------------------- SIDEBAR --------------------
    st.sidebar.title("⚙️ Settings")
    
    model = st.sidebar.selectbox(
        "Select Model",
        [
        "moonshotai/kimi-k2-instruct",
        "groq/compound-mini",
        "meta-llama/llama-4-scout-17b-16e-instruct",
        "meta-llama/llama-prompt-guard-2-22m",
        "canopylabs/orpheus-v1-english",
        "qwen/qwen3-32b",
        "llama-3.3-70b-versatile",
        "llama-3.1-8b-instant",
        "moonshotai/kimi-k2-instruct-0905",
        "meta-llama/llama-prompt-guard-2-86m",
        "whisper-large-v3",
        "openai/gpt-oss-20b",
        "openai/gpt-oss-safeguard-20b",
        "meta-llama/llama-guard-4-12b",
        "meta-llama/llama-4-maverick-17b-128e-instruct",
        "canopylabs/orpheus-arabic-saudi",
        "allam-2-7b",
        "openai/gpt-oss-120b",
        "whisper-large-v3-turbo",
        "groq/compound"
        ]
    )

    temperature = st.sidebar.slider(
    "Temperature",
    min_value=0.0,
    max_value=1.0,
    value=0.3,
    step=0.1
)
   
    return model, temperature 