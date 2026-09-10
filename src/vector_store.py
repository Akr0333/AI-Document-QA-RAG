from pathlib import Path
import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer


class VectorStore:
    def __init__(self, model_name: str):
        self.model = SentenceTransformer(model_name)
        self.index = None
        self.metadata = []

    def build(self, chunks):
        texts = [item["text"] for item in chunks]
        embeddings = self.model.encode(texts, normalize_embeddings=True, show_progress_bar=True).astype("float32")
        self.index = faiss.IndexFlatIP(embeddings.shape[1])
        self.index.add(embeddings)
        self.metadata = chunks

    def search(self, query: str, top_k: int = 5):
        if self.index is None or self.index.ntotal == 0:
            return []
        q = self.model.encode([query], normalize_embeddings=True).astype("float32")
        scores, ids = self.index.search(q, min(top_k, self.index.ntotal))
        return [{**self.metadata[i], "score": float(s)} for s, i in zip(scores[0], ids[0]) if i != -1]

    def save(self, directory: Path):
        directory.mkdir(parents=True, exist_ok=True)
        faiss.write_index(self.index, str(directory / "index.faiss"))
        (directory / "metadata.json").write_text(json.dumps(self.metadata, indent=2), encoding="utf-8")

    def load(self, directory: Path):
        self.index = faiss.read_index(str(directory / "index.faiss"))
        self.metadata = json.loads((directory / "metadata.json").read_text(encoding="utf-8"))
