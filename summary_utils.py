
import google.generativeai as genai

def setup_gemini(api_key):
    genai.configure(api_key=api_key)


def summarize_with_gemini(
    text, 
    model_name="models/gemini-2.5-flash",
    length="medium"  # "short", "medium", "detailed"
):

 # Adjust prompt based on length
    model = genai.GenerativeModel(model_name)

    length_instructions = {
        "Short": "Summarize in 3–5 bullet points with only the most essential facts.",
        "Medium": "Summarize in 5–8 bullet points with clear explanation but no extra details.",
        "Detailed": "Summarize in 10–15 bullet points, including important technical details."
    }


    prompt = (
        f"You are an expert in reading and summarizing academic research papers.\n\n"
        f"{length_instructions[length]}\n\n"
        "The summary should include:\n"
        "• The main problem or goal of the paper\n"
        "• The method/approach used\n"
        "• The key findings/results (if mentioned)\n"
        "• The conclusion or implication\n"
        "• Any important keywords or phrases\n\n"
        "Write in **plain English** so even a non-expert can understand.\n"
        "Use bullet points and make them concise.\n\n"
        "Here is the content to summarize:\n"
        f"---\n{text}\n---"
    )

    try:
        response = model.generate_content(prompt)
        if hasattr(response, "text"):
            return response.text.strip()
        else:
            return "⚠️ No summary generated. Try with a different text."
    except Exception as e:
        return f"❌ Error during summarization: {str(e)}"


def check_relevance_with_gemini(pdf_text, topic, model_name="models/gemini-2.5-pro"):
    
    model = genai.GenerativeModel(model_name)
    prompt = (
        f"You are acting as a strict academic reviewer.\n"
        f"Topic of interest: '{topic}'\n\n"
        f"Rate the relevance of the paper STRICTLY on a scale from 1 (not relevant at all) "
        f"to 10 (perfectly aligned). Avoid giving high scores unless the paper is highly relevant.\n"
        f"Give the result in this format ONLY:\n"
        f"Relevance Score: <score>/10\nReason: <short reason>\n\n"
        f"Generate 5 to 10 concise, relevant tags for this paper.\n\n"
        f"Here is the paper content:\n{pdf_text[:6000]}"
    )
    
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        # Log actual error for debugging but show user-friendly text
        print(f"[Gemini Error] {e}")
        return "⚠️ Unable to check relevance due to an API error."


def generate_answer_with_rag(question, context_chunks, model_name="models/gemini-2.5-pro"):
    if not context_chunks:
        return "I couldn't find relevant information in the stored documents."

    model = genai.GenerativeModel(model_name)
    
    # context = "\n\n".join(context_chunks[:5])  # Use top 5 chunks
    context = "\n\n".join([chunk for chunk, _ in context_chunks[:5]])

    prompt = (
        "You are a careful assistant. Answer ONLY using the provided context.\n"
        "If the answer cannot be found in the context, say exactly:\n"
        "\"I couldn't find the answer in the given documents.\"\n\n"
        f"Context:\n{context}\n\n"
        f"Question:\n{question}\n"
        "Answer:"
    )
    try:
        response = model.generate_content(prompt)
        return response.text.strip() if hasattr(response, "text") and response.text else "No answer generated."
    except Exception as e:
        return f"Error: {str(e)}"



def get_answer_from_pdf(question, embedding_store,model_name="models/gemini-2.5-pro"):
    model = genai.GenerativeModel(model_name)

    relevant_chunks = embedding_store.query(question)
    context = "\n\n".join(relevant_chunks)
    prompt = f"Answer the question based on the following research paper content:\n{context}\n\nQuestion: {question}\nAnswer:"
    try:
        response = model.generate_content(prompt)
        return response.text.strip() if hasattr(response, "text") and response.text else "No answer generated."
    except Exception as e:
        return f"Error: {str(e)}"
    # return ask_openai(prompt)


