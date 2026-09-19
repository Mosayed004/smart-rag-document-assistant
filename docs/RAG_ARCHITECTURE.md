# RAG Architecture

## Overview
The Smart RAG Document Assistant utilizes a standard Retrieval-Augmented Generation (RAG) architecture to answer questions based on the provided PDF documents. This document outlines the key components and data flow of the pipeline.

## Data Flow
1. **Ingestion**: PDF documents are placed in `data/documents/`. 
2. **Extraction**: Text is extracted from each page using `pypdf`.
3. **Cleaning**: Extracted text is normalized by removing duplicate spaces and newlines.
4. **Chunking**: The cleaned text is split into overlapping chunks to preserve context.
5. **Embedding**: Each chunk is converted into a vector representation using a local embedding model.
6. **Storage**: Vectors and metadata are stored persistently in ChromaDB.
7. **Retrieval**: When a query is made, it is embedded, and ChromaDB performs a similarity search to retrieve the most relevant chunks.
8. **Generation**: The retrieved chunks are formatted into a context block and sent to the Ollama LLM, which generates an answer strictly based on the context.

## Chunking Strategy
- **Method**: `RecursiveCharacterTextSplitter`
- **Chunk Size**: 700 characters
- **Chunk Overlap**: 100 characters
- **Reasoning**: A chunk size of 700 ensures that we capture meaningful paragraphs or concepts, while an overlap of 100 characters prevents hard cuts in the middle of sentences or context blocks.

## Embedding Model
- **Model**: `all-MiniLM-L6-v2` (via `sentence-transformers`)
- **Reasoning**: This is a lightweight, highly efficient model that provides excellent semantic matching for general text without requiring heavy GPU resources.

## Vector Database
- **Database**: ChromaDB
- **Storage**: Persistent storage located at `backend/data/vector_store/`
- **Collection**: `science_docs`
- **Metadata**: Each vector stores `source` (filename), `page`, and a unique `chunk_id`.

## Retrieval Process
- **Search Method**: Cosine similarity (HNSW space)
- **Top K**: 4 documents retrieved per query.
- **Filtering**: The system returns the text content alongside metadata to build proper citations.

## Ollama Integration
- **LLM**: `llama3.2:3b`
- **Prompt Strategy**: A strict RAG prompt template is used. It explicitly instructs the model to answer *only* using the provided context and to state "Information not found in the provided documents." if the answer cannot be derived from the chunks. This minimizes hallucinations.
- **Connection**: REST API via `http://localhost:11434/api/generate` with `temperature=0.0` for deterministic outputs.
