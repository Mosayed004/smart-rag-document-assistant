import os
import yaml
import requests
import chromadb
from sentence_transformers import SentenceTransformer

class RAGCore:
    def __init__(self, config_path: str = None):
        if not config_path:
            config_path = os.path.join(os.path.dirname(__file__), '..', '..', 'config.yaml')
            
        with open(config_path, "r", encoding="utf-8") as f:
            self.config = yaml.safe_load(f).get("rag", {})
            
        self.embedding_model_name = self.config.get("embedding_model", "all-MiniLM-L6-v2")
        self.ollama_model = self.config.get("ollama_model", "llama3.2:3b")
        self.collection_name = self.config.get("collection_name", "science_docs")
        self.top_k = self.config.get("top_k", 4)
        self.ollama_url = self.config.get("ollama_url", "http://localhost:11434")
        
        self.embedding_model = None
        self.collection = None

    def _load_embedding_model(self):
        if self.embedding_model is None:
            self.embedding_model = SentenceTransformer(self.embedding_model_name)

    def load_vector_store(self, persist_dir: str = None):
        if not persist_dir:
            persist_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'vector_store')
        
        chroma_client = chromadb.PersistentClient(path=persist_dir)
        try:
            self.collection = chroma_client.get_collection(name=self.collection_name)
        except Exception:
            self.collection = chroma_client.create_collection(
                name=self.collection_name, 
                metadata={"hnsw:space": "cosine"}
            )
            
    def retrieve(self, question: str, top_k: int = None) -> dict:
        if self.collection is None:
            self.load_vector_store()
            
        if self.collection.count() == 0:
            return {"documents": [], "metadatas": [], "distances": []}
            
        self._load_embedding_model()
        query_embedding = self.embedding_model.encode([question]).tolist()
        k = top_k if top_k else self.top_k
        
        results = self.collection.query(
            query_embeddings=query_embedding,
            n_results=min(k, self.collection.count()),
        )
        
        if not results["documents"] or not results["documents"][0]:
             return {"documents": [], "metadatas": [], "distances": []}
             
        return {
            "documents": results["documents"][0],
            "metadatas": results["metadatas"][0],
            "distances": results["distances"][0],
        }

    def build_context(self, documents: list, metadatas: list) -> tuple:
        if not documents:
            return "No documents found.", []
            
        context_parts = []
        sources = []
        for i, (doc, meta) in enumerate(zip(documents, metadatas)):
            source_name = meta.get('source', 'Unknown')
            page_num = meta.get('page', 'Unknown')
            context_parts.append(f"[Source {i+1} from {source_name}, page {page_num}]\n{doc}")
            sources.append(f"{source_name} (Page {page_num})")
            
        # Remove duplicate sources while preserving order
        unique_sources = list(dict.fromkeys(sources))
        return "\n\n".join(context_parts), unique_sources

    def call_ollama(self, prompt: str) -> str:
        url = f"{self.ollama_url}/api/generate"
        payload = {
            "model": self.ollama_model,
            "prompt": prompt,
            "stream": False,
            "options": {"temperature": 0.0}
        }
        try:
            response = requests.post(url, json=payload, timeout=120)
            response.raise_for_status()
            return response.json()["response"].strip()
        except Exception as e:
            return f"Error connecting to Ollama: {e}"

    def rag_query(self, question: str, top_k: int = None) -> dict:
        retrieval = self.retrieve(question, top_k)
        context, sources = self.build_context(retrieval.get("documents", []), retrieval.get("metadatas", []))
        
        prompt_template = """You are a helpful science and history document assistant. Answer the user's question using ONLY the context provided below.

Rules:
- Answer only from provided context
- Do not use outside knowledge
- If information is missing say:
  "Information not found in the provided documents."

Context:
{context}

Question: {question}

Answer:"""
        
        prompt = prompt_template.format(context=context, question=question)
        answer = self.call_ollama(prompt)
        
        return {
            "question": question,
            "answer": answer,
            "sources": sources
        }

# Instantiate a default core for easy importing
rag_core = RAGCore()
