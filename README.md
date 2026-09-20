# 🤖 AI Document Q&A — RAG

An end-to-end Retrieval-Augmented Generation application that answers questions from a user's own documents.

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)
![RAG](https://img.shields.io/badge/AI-RAG-purple)
![FAISS](https://img.shields.io/badge/Vector%20Search-FAISS-green)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-red)

## 🧩 What It Does

Documents are chunked, converted into embeddings, indexed for semantic search, and retrieved as context for an LLM-generated answer.

## 🧠 Architecture

```text
Documents → Chunking → Embeddings → FAISS
Question → Semantic Retrieval → Context → LLM → Answer + Sources
```

## ✨ Key Features

- PDF, TXT and Markdown ingestion
- Document chunking
- Sentence-transformer embeddings
- FAISS similarity search
- Retrieval-Augmented Generation
- Source-aware answers
- Streamlit interface
- Modular Python architecture

## 📁 Structure

```text
AI-Document-QA-RAG/
├── app.py
├── requirements.txt
├── .env.example
├── data/
├── src/
│   ├── config.py
│   ├── document_loader.py
│   ├── vector_store.py
│   ├── rag_pipeline.py
│   └── ingest.py
└── README.md
```

## 🚀 Run

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python src/ingest.py
streamlit run app.py
```

Add your LLM API key to `.env` using the variables documented in `.env.example`.

## 🛠️ Skills

**Python • NLP • Embeddings • Vector Search • FAISS • RAG • Prompt Engineering • LLM APIs • Streamlit**

## 🔮 Roadmap

- Conversational memory
- Reranking
- Hybrid retrieval
- RAG evaluation metrics
- Local LLM support
- Docker deployment

⭐ **Retrieve relevant context. Generate grounded answers.**