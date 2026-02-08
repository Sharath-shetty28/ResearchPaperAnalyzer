import streamlit as st
from groq import Groq
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def combine_summaries(chunk_summaries):
    combined_text = "\n\n".join(chunk_summaries)

    prompt = f"""
You are a senior academic editor and technical writer.

Task:
Combine the following partial summaries into a single, coherent, well-structured final summary.

Guidelines:
- Remove redundancy and repeated points
- Preserve all key technical contributions, methods, and findings
- Maintain logical flow and clarity
- Do NOT introduce new information
- Do NOT hallucinate or speculate
- Use concise, formal academic language
- Write in paragraph form (no bullet points unless necessary)

Partial summaries:
{combined_text}

Final Summary:
"""

    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature,
    )

    return response.choices[0].message.content.strip()