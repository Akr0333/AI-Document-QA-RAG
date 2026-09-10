import sys
from pathlib import Path
import streamlit as st

ROOT = Path(__file__).resolve().parent
sys.path.append(str(ROOT / "src"))

from config import INDEX_DIR, EMBEDDING_MODEL, TOP_K, OPENAI_API_KEY, OPENAI_MODEL
from vector_store import VectorStore
from rag_pipeline import answer_question

st.set_page_config(page_title="AI Document Q&A", page_icon="🤖", layout="wide")
st.title("🤖 AI Document Q&A Assistant")
st.caption("RAG • Embeddings • FAISS • LLM")

store = VectorStore(EMBEDDING_MODEL)
if not (INDEX_DIR / "index.faiss").exists():
    st.info("Add PDF/TXT/Markdown files to data/ and run: python src/ingest.py")
    st.stop()
store.load(INDEX_DIR)

question = st.text_input("Ask a question about your documents")
if question:
    results = store.search(question, TOP_K)
    if OPENAI_API_KEY:
        with st.spinner("Retrieving context and generating an answer..."):
            st.subheader("Answer")
            st.write(answer_question(question, results, OPENAI_API_KEY, OPENAI_MODEL))
    else:
        st.warning("Set OPENAI_API_KEY in .env to enable answer generation.")
    st.subheader("Retrieved Sources")
    for item in results:
        with st.expander(f"{item['source']} • similarity={item['score']:.3f}"):
            st.write(item['text'])
