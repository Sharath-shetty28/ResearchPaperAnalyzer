from config.setting import CHUNK_SIZE, CHUNK_OVERLAP, TOP_K

def chunk_text(text, chunk_size=CHUNK_SIZE, overlap=CHUNK_OVERLAP):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start = end - overlap
    return chunks


def filter_chunks(chunks, topic, top_k=TOP_K):
    scored = []
    for chunk in chunks:
        score = sum(
            1 for word in topic.lower().split()
            if word in chunk.lower()
        )
        if score > 0:
            scored.append((score, chunk))
    scored.sort(reverse=True, key=lambda x: x[0])
    return [chunk for _, chunk in scored[:top_k]]
