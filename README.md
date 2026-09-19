# Smart RAG Document Assistant

## Overview
The Smart RAG Document Assistant is an advanced Retrieval-Augmented Generation (RAG) system built to answer questions accurately by extracting facts from a local corpus of PDF files. The pipeline is fully deterministic and avoids hallucinations by anchoring generation entirely to retrieved context. 

The core flow is: 
`PDF documents → text extraction → cleaning → recursive chunking → local embeddings → ChromaDB → semantic retrieval → Ollama → grounded answer + sources.`

## Current Status
**The core RAG backend is 100% complete and ready for integration.** 

**Completed:**
- Complete RAG core logic
- Refined dataset (5 scientific/historical PDFs, 15 pages)
- Chroma persisted vector store with clean indexing
- Local LLM generation via Ollama (`llama3.2:3b`)
- Automated 10-question evaluation suite
- Fully decoupled, reusable `rag_core.py` module

**Pending:**
- FastAPI API wiring
- Frontend user interface
- API tests
- Final demo video and deployment

## Architecture
```text
PDF Documents
      ↓
    PyPDF
      ↓
  Cleaning
      ↓
Recursive Chunking
      ↓
all-MiniLM-L6-v2 (Embeddings)
      ↓
  ChromaDB
      ↓
  Retriever
      ↓
   Context
      ↓
Ollama llama3.2:3b
      ↓
Answer + Sources
```

## Tech Stack
- **Python 3.12**
- **Jupyter**
- **PyPDF**
- **LangChain Text Splitters**
- **Sentence Transformers**
- **all-MiniLM-L6-v2**
- **ChromaDB**
- **Ollama**
- **llama3.2:3b**
- **Pandas**
- **FastAPI** (planned/in progress)
- **Streamlit or Gradio** (planned/in progress)

## Dataset
The system operates on an expansive high-quality corpus of 5 realistic PDF files totaling 15 pages of rich data.
- **Topics include**: Machine Learning, Quantum Mechanics, Ancient Egypt, Nutrition, and Climate Change.

## RAG Configuration
The RAG pipeline operates under the following fine-tuned parameters (managed in `backend/config.yaml`):
- `chunk_size` = 700
- `chunk_overlap` = 100
- `embedding_model` = all-MiniLM-L6-v2
- `ollama_model` = llama3.2:3b
- `collection_name` = science_docs
- `top_k` = 4

## RAG Usage
The RAG module is fully abstracted. Backend developers can natively query the system by importing the singleton:

```python
from backend.app.services.rag_core import rag_core

response = rag_core.rag_query("What is machine learning?")
# { "question": "...", "answer": "...", "sources": [...] }
```

## Evaluation
The pipeline includes a fully automated deterministic evaluation process:
- Tests against 10 diverse questions (Normal, Complex, Out-of-Domain).
- Verifies grounded context ingestion.
- Ensures the LLM respectfully rejects out-of-domain prompts.
- All evaluation results are automatically exported to `notebooks/evaluation_results.csv`.

## Setup
To initialize the RAG module locally:

1. Create a Python virtual environment: `python -m venv .venv`
2. Activate the environment and install requirements: `pip install -r backend/requirements.txt`
3. Download and install [Ollama](https://ollama.com/)
4. Pull the target model: `ollama pull llama3.2:3b`
5. Execute the evaluation notebook: Run `notebooks/rag_pipeline.ipynb` to verify your environment.

## Next Development Stage
**The next developer should build the FastAPI layer and frontend using the existing `rag_core.py`.** The RAG pipeline requires no further tuning for the backend endpoints to be scaffolded.
