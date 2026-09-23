from fastapi.testclient import TestClient

from app.main import app
from app.services.rag_core import rag_core


client = TestClient(app)


def test_query_happy_path(monkeypatch):
    def fake_rag_query(question: str):
        return {
            "question": question,
            "answer": "This is a test answer.",
            "sources": ["test_document.pdf (Page 1)"],
        }

    monkeypatch.setattr(rag_core, "rag_query", fake_rag_query)

    response = client.post(
        "/query",
        json={"question": "What is this document about?"},
    )

    assert response.status_code == 200

    data = response.json()

    assert data["answer"] == "This is a test answer."
    assert data["sources"] == ["test_document.pdf (Page 1)"]


def test_query_invalid_request():
    response = client.post(
        "/query",
        json={},
    )

    assert response.status_code == 422