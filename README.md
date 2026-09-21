# 🤖 AI Document Q&A — RAG

An end-to-end **Retrieval-Augmented Generation (RAG)** application that answers questions from a user's documents using semantic retrieval and an LLM.

## 🎯 Problem

Traditional document search often requires users to find information manually.

This project builds a workflow where a user can provide documents, ask a natural-language question, retrieve relevant context and receive a grounded answer.

## 🧠 Architecture

```text
Documents
   ↓
Chunking
   ↓
Embeddings
   ↓
FAISS Vector Search
   ↓
Relevant Context
   ↓
LLM
   ↓
Answer + Sources
```

## ✨ Features

- PDF, TXT and Markdown ingestion
- Document chunking
- Sentence-transformer embeddings
- FAISS similarity search
- Retrieval-Augmented Generation
- Source-aware answers
- Streamlit interface
- Modular Python architecture

## 🛠️ Skills Demonstrated

**Python • NLP • Embeddings • Vector Search • FAISS • RAG • Prompt Engineering • LLM APIs • Streamlit**

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

## 🚀 Run Locally

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python src/ingest.py
streamlit run app.py
```

Add the required LLM API key to `.env` using the variables documented in `.env.example`.

## 🔮 Roadmap

- Conversational memory
- Retrieval reranking
- Hybrid retrieval
- RAG evaluation metrics
- Local LLM support
- Docker deployment

> Portfolio project demonstrating an applied AI/NLP workflow. No API keys or secrets are stored in the repository.

⭐ **Retrieve relevant context → Generate grounded answers**
