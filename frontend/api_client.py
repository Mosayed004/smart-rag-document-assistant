import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv("API_BASE_URL")

if not API_URL:
    raise RuntimeError(
        "API_BASE_URL is not configured. "
        "Create frontend/.env with API_BASE_URL=http://localhost:8000"
    )


def ask_question(question: str, top_k: int = 4):
    response = requests.post(
        f"{API_URL}/query",
        json={
            "question": question,
            "top_k": top_k,
        },
        timeout=120,
    )

    response.raise_for_status()
    return response.json()
