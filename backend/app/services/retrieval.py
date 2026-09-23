from typing import Optional

from app.services.rag_core import rag_core


class RetrievalService:
    """
    Handles document retrieval from the vector database.
    """

    def __init__(self):
        self.rag_core = rag_core

    def retrieve(
        self,
        question: str,
        top_k: Optional[int] = None
    ) -> dict:
        """
        Retrieve the most relevant documents for a question.
        """
        return self.rag_core.retrieve(
            question=question,
            top_k=top_k
        )

    def build_context(
        self,
        documents: list,
        metadatas: list
    ) -> tuple:
        """
        Build context and source list from retrieved documents.
        """
        return self.rag_core.build_context(
            documents=documents,
            metadatas=metadatas
        )


retrieval_service = RetrievalService()