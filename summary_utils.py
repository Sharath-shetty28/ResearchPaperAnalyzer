from prompts.length_instruction import length_instruction
from prompts.summarize import sumarrys
from prompts.ratings import ratings
from prompts.generate_answer import answers
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

    length_instructions = length_instruction()

    prompt = sumarrys()

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
    ratings = ratings(pdf_text,topic)
    
    try:
        response = model.generate_content(ratings)
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

    answer = answers(context,question)
    try:
        response = model.generate_content(answer)
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


