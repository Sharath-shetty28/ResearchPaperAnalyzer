import chromadb
import uuid
from chromadb.config import Settings

from core.embeddings import get_embedding
from config.settings import CHROMA_DIR, COLLECTION_NAME

# ---- Chroma Client ----
chroma_client = chromadb.Client(
    Settings(
        persist_directory=CHROMA_DIR,
        anonymized_telemetry=False
    )
)

# ---- Collection ----
collection = chroma_client.get_or_create_collection(
    name=COLLECTION_NAME
)

# ---- Add PDF chunks ----
def add_pdf_chunks(pdf_name, chunks):
    collection.add(
        documents=chunks,
        embeddings=[get_embedding(chunk) for chunk in chunks],
        metadatas=[
            {"pdf_name": pdf_name, "chunk_index": i}
            for i in range(len(chunks))
        ],
        ids=[str(uuid.uuid4()) for _ in chunks]
    )

# ---- Retrieve relevant chunks ----
def retrieve_chunks(topic, k=3):
    topic_embedding = get_embedding(topic)

    results = collection.query(
        query_embeddings=[topic_embedding],
        n_results=k
    )

    return results["documents"][0]