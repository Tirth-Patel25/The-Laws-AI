from langchain_experimental.text_splitter import SemanticChunker
from services.embedder import embedder

semanticChunker = SemanticChunker(embeddings=embedder, breakpoint_threshold_amount=0.75, min_chunk_size=2000)

# <----- Type wise Chunks ----->
def get_judgement_chunks(text: str) -> list[str]:
    splitted_texts = text.split("# SEPERATOR #")
    # splitted_texts.pop()
    return splitted_texts

def get_act_chunks(text: str) -> list[str]:
    splitted_texts = text.split("# SEPERATOR #")

def get_order_chunks(text: str) -> list[str]:
    splitted_texts = text.split("# SEPERATOR #")
    # splitted_texts.pop()
    return splitted_texts

# <----- Chunks ----->
def chunker(text: str, category: str) -> list[str]:
    if category == "judgement":
        chunks = get_judgement_chunks(text)
        return chunks
    
    elif category == "order":
        chunks = get_order_chunks(text)
        return chunks

    else:
        chunks = [text]
        return chunks

# <----- File IDs ----->
def create_ids(name: str, length: int) -> list[str]:
    return [f"{name}_@_{i}" for i in range(1, length+1)]