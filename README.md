# AI Document Q&A Assistant (RAG) 🤖

An end-to-end **Retrieval-Augmented Generation (RAG)** application that answers questions from your own documents.

## ✨ What it demonstrates

- Document ingestion and chunking
- Sentence-transformer embeddings
- FAISS vector similarity search
- Retrieval-Augmented Generation
- Prompt engineering
- Streamlit interface
- Source-aware responses
- Modular AI engineering structure

## 🧠 Architecture

```text
Documents → Chunking → Embeddings → FAISS
                                  ↓
Question → Semantic Retrieval → Context → LLM → Answer + Sources
```

## 📁 Structure

```text
AI-Document-QA-RAG/
├── app.py
├── requirements.txt
├── .gitignore
├── .env.example
├── README.md
├── data/
│   └── README.md
└── src/
    ├── config.py
    ├── document_loader.py
    ├── vector_store.py
    ├── rag_pipeline.py
    └── ingest.py
```

## 🚀 Setup

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
pip install -r requirements.txt
```

Copy `.env.example` to `.env` and add your LLM API key.

## ▶️ Run

Add `.pdf`, `.txt`, or `.md` files to `data/`, then:

```bash
python src/ingest.py
streamlit run app.py
```

## 🎯 Example use cases

- College notes and syllabus assistant
- Research-paper Q&A
- Company policy assistant
- Personal knowledge base
- Technical documentation chatbot

## 💼 Skills demonstrated

**Python • NLP • Embeddings • Vector Search • FAISS • RAG • Prompt Engineering • LLM APIs • Streamlit**

## 🔮 Future Improvements

- Conversational memory
- Reranking
- Hybrid retrieval
- RAG evaluation metrics
- Local LLM support
- Docker and cloud deployment

---
⭐ Built as a practical AI engineering portfolio project.
