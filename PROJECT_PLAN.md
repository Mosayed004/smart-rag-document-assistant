# Smart RAG Document Assistant — Project Plan

---

## Phase 0: Setup
- [x] Create project folder structure
- [ ] Initialize Git repository
- [ ] Set up Python virtual environments (backend & frontend)
- [ ] Install base dependencies
- [ ] Configure `.env` files from `.env.example` templates

---

## Phase 1: Dataset
- [ ] Collect and organize source documents (PDF, TXT, DOCX)
- [ ] Place raw documents in `data/documents/`
- [ ] Validate document formats and encoding
- [ ] Document the dataset sources and licensing

---

## Phase 2: RAG Pipeline
- [ ] Implement document loading (PDF, TXT loaders)
- [ ] Implement text chunking strategy (recursive character splitting)
- [ ] Generate embeddings using OpenAI or HuggingFace models
- [ ] Store embeddings in ChromaDB / FAISS vector store
- [ ] Build retrieval chain (query → vector search → top-K results)
- [ ] Build generation chain (context + query → LLM → answer)
- [ ] Prototype and validate end-to-end in `notebooks/rag_pipeline.ipynb`

---

## Phase 3: Backend
- [ ] Set up FastAPI application with CORS and health check
- [ ] Define Pydantic schemas for query request/response
- [ ] Implement retrieval service (`services/retrieval.py`)
- [ ] Implement generation service (`services/generation.py`)
- [ ] Create `/api/v1/query` endpoint
- [ ] Add structured logging
- [ ] Write unit tests (`tests/test_query.py`)

---

## Phase 4: Frontend
- [ ] Build Streamlit chat interface (`app.py`)
- [ ] Implement API client to communicate with backend (`api_client.py`)
- [ ] Display answers with source attribution
- [ ] Add configuration sidebar (top-K, model settings)
- [ ] Handle error states and loading indicators

---

## Phase 5: Testing and Deployment
- [ ] Run backend unit and integration tests
- [ ] Test full end-to-end flow (frontend → backend → LLM)
- [ ] Build Docker image for backend
- [ ] Write deployment documentation
- [ ] Final review and cleanup
