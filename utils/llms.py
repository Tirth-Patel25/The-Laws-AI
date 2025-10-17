from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
load_dotenv()

# from langchain_ollama import ChatOllama

def get_llm():
    # Local Testing
    return ChatGroq(api_key=os.getenv("GROQ_API_KEY"), model=os.getenv("GROQ_MODEL_NAME"), temperature=0, max_tokens=None)

    # Production
    # return ChatOllama(model="llama3.1:8b", base_url="http://192.168.29.156:11434")

def llm_with_tool(*args):
    llm=get_llm()
    tools=list(args)
    return llm.bind_tools(tools, tool_choice="auto")
