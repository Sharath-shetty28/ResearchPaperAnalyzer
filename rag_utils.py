import chromadb
from chromadb.utils import embedding_functions
from uuid import uuid4
import streamlit as st
import time

# Persistent ChromaDB folder
PERSIST_DIR = "./chroma_storage"
embedding_fn = embedding_functions.DefaultEmbeddingFunction()
client = chromadb.PersistentClient(path=PERSIST_DIR)

def get_user_collection(user_id):
    return client.get_or_create_collection(
        f"research_papers_{user_id}",  # unique collection name per user
        embedding_function=embedding_fn
    )

# Example: get a collection for current user
collection = get_user_collection(user_id="user123")

# client.delete_collection(f"research_papers_{user_id}")


# ===== TEXT CHUNKER =====
def chunk_text(text, chunk_size=800, overlap=100):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks

# ===== QUERY =====
def expand_query_if_short(query):
    query = query.strip()

    # If query is empty or nonsense
    if not query:
        return "Explain the key insights from the uploaded documents."

    # If it's short, expand it
    if len(query.split()) <= 3:
        # Optional synonyms to boost semantic search
        synonyms = {
            "dataset": "dataset, data collection, training set",
            "tags": "tags, labels, annotations",
            "model": "model, algorithm, architecture"
        }

        expanded_terms = []
        for word in query.split(","):
            word = word.strip().lower()
            expanded_terms.append(synonyms.get(word, word))

        return f"Explain the meaning, purpose, and importance of {', '.join(expanded_terms)} in the context of the uploaded documents."

    return query


# ===== ADD PDF TO CHROMADB =====
def add_pdf_to_chromadb(text, source_name):
    chunks = chunk_text(text)
    chunks = [c.strip() for c in chunks if c.strip()]
    if not chunks:
        print(f"⚠️ No valid chunks found for {source_name}")
        return

    # Ensure unique source name in case same PDF name is uploaded again

    timestamped_source = f"{source_name}_{int(time.time())}"

    ids = [str(uuid4()) for _ in chunks]
    metadatas = [{"source": timestamped_source, "chunk_id": i} for i in range(len(chunks))]

    try:
        collection.add(documents=chunks, metadatas=metadatas, ids=ids)
    except Exception as e:
        print(f"❌ Error adding PDF to ChromaDB: {e}")


# ===== SEARCH CHROMADB (Unique Results + Fallbacks) =====
# def query_chromadb(question, top_k=5):
#     try:
#         results = collection.query(query_texts=[question], n_results=top_k *3)
#     except Exception as e:
#         print(f"❌ ChromaDB query error: {e}")
#         return []

#     # Gracefully handle missing or empty results
#     if not results or "documents" not in results or not results["documents"]:
#         print("⚠️ No results found.")
#         return []

#     docs = results.get("documents", [[]])[0]
#     metas = results.get("metadatas", [[]])[0]

#     # Deduplicate by content + source + chunk_id
#     seen = set()
#     unique_results = []
#     for doc, meta in zip(docs, metas):
#         if not doc or not meta:
#             continue
#         key = (doc.strip(), meta.get("source", ""), meta.get("chunk_id", ""))
#         if key not in seen:
#             seen.add(key)
#             unique_results.append((doc.strip(), meta))

#     return unique_results

def query_chromadb(question, top_k=5):
    results = collection.query(query_texts=[question], n_results=top_k * 3)  
    docs = results["documents"][0]
    metas = results["metadatas"][0]

    seen_texts = set()
    unique_results = []

    for doc, meta in zip(docs, metas):
        normalized_doc = " ".join(doc.strip().split())  # normalize spaces
        if normalized_doc not in seen_texts:
            seen_texts.add(normalized_doc)
            unique_results.append((doc, meta))

        if len(unique_results) >= top_k:
            break

    return unique_results

def clear_chroma_storage():
    collection.delete(where={"source": {"$ne": None}})
    st.success("✅ All stored PDFs cleared!")