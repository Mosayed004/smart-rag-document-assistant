# Smart RAG Document Assistant

An intelligent document assistant powered by Retrieval-Augmented Generation (RAG). Upload your documents, ask questions in natural language, and get accurate answers grounded in your own data — with source references.

---

## 📁 Project Structure

```text
rag-assistant-project/
│
├── notebooks/
│   └── rag_pipeline.ipynb          # Experimentation & prototyping
│
├── backend/
│   ├── app/
│   │   ├── main.py                 # FastAPI entry point
│   │   ├── api/routes/query.py     # Query endpoint
│   │   ├── core/config.py          # App configuration
│   │   ├── schemas/query.py        # Request/response models
│   │   ├── services/
│   │   │   ├── retrieval.py        # Document retrieval service
│   │   │   └── generation.py       # LLM generation service
│   │   └── utils/logging_config.py # Logging setup
│   │
│   ├── data/vector_store/          # Persisted vector database
│   ├── tests/test_query.py         # API tests
│   ├── requirements.txt
│   ├── .env.example
│   └── Dockerfile
│
├── frontend/
│   ├── app.py                      # Streamlit UI
│   ├── api_client.py               # Backend API client
│   ├── .env.example
│   └── requirements.txt
│
├── data/
│   └── documents/                  # Raw input documents
│
├── .gitignore
├── PROJECT_PLAN.md
└── README.md
```

---

## 🔑 Key Features

- **Document Ingestion** — Load PDFs, text files, and other document formats
- **Semantic Chunking** — Split documents into meaningful chunks for embedding
- **Vector Search** — Fast similarity search using ChromaDB / FAISS
- **LLM-Powered Answers** — Generate accurate, context-grounded responses
- **Source Attribution** — Every answer includes references to source documents
- **Chat Interface** — Interactive Streamlit frontend with conversation history

---

## 🛠️ Tech Stack

| Layer      | Technology                    |
|------------|-------------------------------|
| Backend    | FastAPI, Uvicorn              |
| Frontend   | Streamlit                     |
| LLM        | OpenAI / Ollama               |
| Embeddings | OpenAI / HuggingFace          |
| Vector DB  | ChromaDB / FAISS              |
| Notebook   | Jupyter                       |
| Container  | Docker                        |

---

## 📋 Project Phases

See [PROJECT_PLAN.md](./PROJECT_PLAN.md) for the full development roadmap.
