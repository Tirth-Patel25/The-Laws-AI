from langchain_ollama import ChatOllama
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from services.prompts import Prompt
from typing import Tuple
import os
from utils.llm import get_llm

load_dotenv()

# Production Local LLM use
# ollama_llm = ChatOllama(model=os.getenv("OLLAMA_MODEL", "llama3.1:8b"))

# Local
def llm(query: str, chat_history: list[dict], context: str = "No Context Found Do not response") -> Tuple[str, str]:
    prompt = Prompt.response_prompt(context=context)
    promptm={"role":"human","content":prompt}
    chat_history.insert(0,promptm)
    querym={"role":"human","content":query}
    chat_history.append(querym)
    messages = chat_history
    generation = get_llm().invoke(messages)
    # print("\n",generation,"\n")
    response = generation.content
    # print(generation)
    # tokens = generation.response_metadata["token_usage"]["total_tokens"]
    tokens=generation.usage_metadata["total_tokens"]
    return response,tokens