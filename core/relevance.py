from groq import Groq

client = Groq(api_key="your_api_key")

def build_relevance_prompt(topic, chunks):
    context = "\n\n".join(chunks)

    return f"""
You are a strict academic reviewer.

Topic:
"{topic}"

Relevant sections:
{context}

Output format ONLY:
Relevance Score: X/10
Tags: tag1, tag2
Justification: one line
"""

def get_relevance(topic, chunks):
    prompt = build_relevance_prompt(topic, chunks)

    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature
    )

    return response.choices[0].message.content.strip()