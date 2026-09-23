from fastapi import APIRouter, HTTPException

from app.schemas.query import QueryRequest, QueryResponse
from app.services.rag_core import rag_core


router = APIRouter()


@router.post("/query", response_model=QueryResponse)
def query_documents(request: QueryRequest):
    try:
        result = rag_core.rag_query(request.question)

        return QueryResponse(
            answer=result["answer"],
            sources=result["sources"],
        )

    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=f"Error processing query: {exc}",
        )