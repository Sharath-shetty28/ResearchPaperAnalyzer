from prompts.summarize import build_summary_prompt
from groq import Groq
import streamlit as st
import os
from config.settings import CHUNK_SIZE, CHUNK_OVERLAP

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def chunk_text(text, chunk_size=CHUNK_SIZE, overlap=CHUNK_OVERLAP):
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start = end - overlap

    return chunks


def summarize_chunk(chunk, summary_length):
    prompt = build_summary_prompt(chunk, summary_length)

    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature,
    )

    return response.choices[0].message.content.strip()