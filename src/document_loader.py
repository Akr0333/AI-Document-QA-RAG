from pathlib import Path
from pypdf import PdfReader


def load_documents(data_dir: Path):
    documents = []
    for path in sorted(data_dir.glob("*.txt")):
        text = path.read_text(encoding="utf-8", errors="ignore").strip()
        if text:
            documents.append({"source": path.name, "text": text})
    for path in sorted(data_dir.glob("*.md")):
        text = path.read_text(encoding="utf-8", errors="ignore").strip()
        if text:
            documents.append({"source": path.name, "text": text})
    for path in sorted(data_dir.glob("*.pdf")):
        reader = PdfReader(str(path))
        text = "\n".join(page.extract_text() or "" for page in reader.pages).strip()
        if text:
            documents.append({"source": path.name, "text": text})
    return documents


def chunk_text(text: str, chunk_size: int = 700, overlap: int = 120):
    words = text.split()
    chunks = []
    start = 0
    while start < len(words):
        end = min(start + chunk_size, len(words))
        chunks.append(" ".join(words[start:end]))
        if end == len(words):
            break
        start = max(0, end - overlap)
    return chunks
