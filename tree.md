# 📁 Project Tree — Smart RAG Document Assistant

```text
rag-assistant-project/
│
├── .gitignore
├── README.md
├── PROJECT_PLAN.md
│
├── data/
│   └── documents/                      # Raw input documents (PDF, TXT, DOCX)
│
├── notebooks/
│   └── rag_pipeline.ipynb              # Jupyter notebook for RAG experimentation
│
├── backend/
│   ├── .env.example                    # Backend environment variables template
│   ├── requirements.txt                # Backend Python dependencies
│   ├── Dockerfile                      # Docker container definition
│   │
│   ├── app/
│   │   ├── main.py                     # FastAPI application entry point
│   │   │
│   │   ├── api/
│   │   │   └── routes/
│   │   │       └── query.py            # /query API endpoint
│   │   │
│   │   ├── core/
│   │   │   └── config.py              # App settings & env loading
│   │   │
│   │   ├── schemas/
│   │   │   └── query.py               # Pydantic request/response models
│   │   │
│   │   ├── services/
│   │   │   ├── retrieval.py           # Document retrieval service
│   │   │   └── generation.py          # LLM generation service
│   │   │
│   │   └── utils/
│   │       └── logging_config.py      # Logging configuration
│   │
│   ├── data/
│   │   └── vector_store/              # Persisted vector database
│   │
│   └── tests/
│       └── test_query.py              # Backend API tests
│
└── frontend/
    ├── .env.example                    # Frontend environment variables template
    ├── requirements.txt                # Frontend Python dependencies
    ├── app.py                          # Streamlit chat interface
    └── api_client.py                   # HTTP client for backend API
```

