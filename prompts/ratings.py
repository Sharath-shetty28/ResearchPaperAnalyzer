def ratings(pdf_text, topic):
    ratings = (
        f"You are acting as a strict academic reviewer.\n"
        f"Topic of interest: '{topic}'\n\n"
        f"Rate the relevance of the paper STRICTLY on a scale from 1 (not relevant at all) "
        f"to 10 (perfectly aligned). Avoid giving high scores unless the paper is highly relevant.\n"
        f"Give the result in this format ONLY:\n"
        f"Relevance Score: <score>/10\nReason: <short reason>\n\n"
        f"Generate 5 to 10 concise, relevant tags for this paper.\n\n"
        f"Here is the paper content:\n{pdf_text[:6000]}"
    )
    return ratings