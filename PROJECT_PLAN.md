# Project Plan: Smart RAG Document Assistant

## Phase 0: Setup
- [x] Define project structure
- [x] Set up Git repository and basic documentation
- [x] Create Python virtual environment and `requirements.txt`
- [x] Install core dependencies (LangChain, PyPDF, SentenceTransformers, ChromaDB)
- [x] Set up and verify local Ollama LLM execution

## Phase 1: Dataset
- [x] Collect high-quality scientific and historical PDFs
- [x] Organize files into `data/documents`
- [x] Validate documents (currently 5 PDFs, 15 pages in use)

## Phase 2: RAG Pipeline (COMPLETE - READY FOR BACKEND)
- [x] Load and parse PDF documents programmatically
- [x] Extract raw text
- [x] Preserve metadata (source, page, document_id)
- [x] Clean and normalize text
- [x] Chunk documents (RecursiveCharacterTextSplitter)
- [x] Generate embeddings (`all-MiniLM-L6-v2`)
- [x] Initialize ChromaDB
- [x] Create persistent vector store
- [x] Implement semantic retrieval logic
- [x] Integrate Ollama generation (`llama3.2:3b`)
- [x] Write grounded prompt with accurate source attribution
- [x] Build 10-question evaluation suite (Normal, Difficult, Out-of-Domain)
- [x] Export automated evaluation to `evaluation_results.csv`
- [x] Refactor pipeline into reusable `rag_core.py` module
- [x] Author comprehensive `RAG_ARCHITECTURE.md` documentation
- [x] Verify pipeline stability via full `Restart Kernel -> Run All` execution

**RAG MODULE STATUS: COMPLETE / READY FOR BACKEND.**

## Phase 3: Backend (Pending Implementation)
- [ ] Initialize FastAPI main app
- [ ] Implement `GET /health` endpoint
- [ ] Implement `POST /query` endpoint
- [ ] Define robust Pydantic schemas
- [ ] Configure CORS middleware
- [ ] Wire up lifespan startup events for RAG loading
- [ ] Integrate retrieval and generation services with `rag_core.py`
- [ ] Write integration and unit backend tests
- [ ] Complete production Dockerfile

## Phase 4: Frontend (Pending Implementation)
- [ ] Scaffold Streamlit / Gradio UI
- [ ] Implement API client wrapper
- [ ] Render answers and cited sources
- [ ] Implement robust loading states and error handling

## Phase 5: Final Delivery
- [ ] Update final README after backend/frontend completion
- [ ] Gather UI screenshots
- [ ] Record end-to-end demo video
- [ ] Prepare final presentation
- [ ] Conduct final fresh-clone functionality test
