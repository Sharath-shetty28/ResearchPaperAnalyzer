
def answers(context,question):
    prompt = (
        "You are a careful assistant. Answer ONLY using the provided context.\n"
        "If the answer cannot be found in the context, say exactly:\n"
        "\"I couldn't find the answer in the given documents.\"\n\n"
        f"Context:\n{context}\n\n"
        f"Question:\n{question}\n"
        "Answer:"
    )
    return answers