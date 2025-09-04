from langchain_ollama import ChatOllama
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage
from dotenv import load_dotenv
from services.prompts import Prompt
from typing import Tuple
import os

load_dotenv()

# Production Local LLM use
# ollama_llm = ChatOllama(model=os.getenv("OLLAMA_MODEL", "llama3.1:8b"))

# Local
ollama_llm = ChatGroq(api_key=os.getenv("GROQ_API_KEY"), model="llama-3.3-70b-versatile", temperature=0, max_tokens=None)

def llm(query: str, context: str = "No Context Found Do not response") -> Tuple[str, str]:
    prompt = Prompt.response_prompt(context=context)
    messages = [HumanMessage(content=prompt), HumanMessage(content=query)]
    generation = ollama_llm.invoke(messages)
    response = generation.content
    tokens = generation.usage.total_tokens
    return response, tokens