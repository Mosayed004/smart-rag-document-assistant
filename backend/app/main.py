from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes.query import router as query_router
from app.core.config import settings
from app.services.rag_core import rag_core


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the persisted vector store once when the API starts.
    rag_core.load_vector_store()

    app.state.rag_core = rag_core

    yield


app = FastAPI(
    title=settings.app_name,
    version="1.0.0",
    lifespan=lifespan,
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.frontend_origin],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": settings.app_name,
    }


app.include_router(query_router)