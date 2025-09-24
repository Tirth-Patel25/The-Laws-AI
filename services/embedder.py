# from langchain_ollama import OllamaEmbeddings
import os
from dotenv import load_dotenv
from langchain_nomic import NomicEmbeddings

load_dotenv()

# embedder = OllamaEmbeddings(model="nomic-embed-text", base_url=os.getenv("OLLAMA_BASE_URL"))
# embedder = OllamaEmbeddings(model="jina/jina-embeddings-v2-base-en", base_url=os.getenv("OLLAMA_BASE_URL"))
embedder=NomicEmbeddings(model="nomic-embed-text-v1.5",nomic_api_key=os.getenv("NOMIC_API_KEY"))

def generate_embeddings(chunks: list[str]):
    embeddings = embedder.embed_documents(texts=chunks)
    return embeddings

def search_embeddings(query: str) -> list[float]:
    embeddings = embedder.embed_query(text=query)
    return embeddings

def text_from_embeddings(embeddings: list[float]) -> str:
    text = embedder(text=embeddings)
    return text