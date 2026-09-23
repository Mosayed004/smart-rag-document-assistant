from app.services.rag_core import rag_core


class GenerationService:
    """
    Handles answer generation using the configured LLM.
    """

    def __init__(self):
        self.rag_core = rag_core

    def generate(self, prompt: str) -> str:
        """
        Send a prompt to the configured Ollama model.
        """
        return self.rag_core.call_ollama(prompt)


generation_service = GenerationService()