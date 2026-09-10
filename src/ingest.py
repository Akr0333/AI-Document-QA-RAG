from config import DATA_DIR, INDEX_DIR, EMBEDDING_MODEL, CHUNK_SIZE, CHUNK_OVERLAP
from document_loader import load_documents, chunk_text
from vector_store import VectorStore


def main():
    docs = load_documents(DATA_DIR)
    if not docs:
        print("No .pdf, .txt or .md documents found in data/")
        return
    chunks = []
    for doc in docs:
        for i, text in enumerate(chunk_text(doc["text"], CHUNK_SIZE, CHUNK_OVERLAP)):
            chunks.append({"source": doc["source"], "chunk_id": i, "text": text})
    store = VectorStore(EMBEDDING_MODEL)
    store.build(chunks)
    store.save(INDEX_DIR)
    print(f"Indexed {len(docs)} documents into {len(chunks)} chunks.")


if __name__ == "__main__":
    main()
