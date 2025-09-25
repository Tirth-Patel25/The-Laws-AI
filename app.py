from fastapi import FastAPI, HTTPException, Body, File, UploadFile
from fastapi.responses import JSONResponse
from langchain_core.messages import HumanMessage
from fastapi.middleware.cors import CORSMiddleware

# Custom Imports
from utils.llms import llm_with_tool
from services.tools import judgement, act, order
from services.milvus_services import insert, search
from services.llm_response import llm

# Environment config imports
from dotenv import load_dotenv
import os
load_dotenv()

# <----- FastAPI ----->
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# <----- ENDPOINTS ----->
@app.get("/")
async def root():
    return JSONResponse(content="Hello from The Laws!!!", status_code=200)

# <----- File Upload ----->
@app.post("/upload")
async def ask(category: str, file: UploadFile = File(...)):
    file_name = file.filename
    allowed_extensions = ["pdf", "json"]
    file_extension = file_name.split(".")[-1]
    f_name = file_name.split(".")[0]

    if file_extension not in allowed_extensions:
        raise HTTPException(detail="Unsupported file format!!!", status_code=400)
    
    if not category:
        return HTTPException(detail="Category Not mentioned!!!", status_code=400)
    
    response = insert(collection=category, file_name=f_name, file_type=file_extension, file=file)
    if response:
        return JSONResponse(content="success", status_code=200)
    else:
        raise HTTPException(detail="There was an error inserting Data", status_code=400)

# <----- Chat ----->
@app.post("/chat")
async def chat(request: dict =  Body(...)):
    query = request.get("query")
    tool_llama = llm_with_tool(judgement, act, order)
    chat_history = request.get("chat_history", [])
    prompt = f"""You are an Legal AI assistant with access to the following tools:
    1. judgement: Use this tool to retrieve or summarize Indian court judgments.
    2. act: Use this tool to provide details about Indian Acts and their sections.
    3. order: Use this tool to fetch or explain Indian government or court orders.

    Instructions:
    - When a user query matches the function of a tool, CALL the tool immediately
    - Do NOT just suggest which tool could be called.
    - Only if the query does NOT match any tool, respond normally.

    Query:
    {query}
    """
    chat_history.append(HumanMessage(content=prompt))
    res = tool_llama.invoke(chat_history)
    initial_tokens = res.usage_metadata["total_tokens"]
    
    if res.tool_calls and res.tool_calls[0]:
        tool_call = res.tool_calls[0]
        context = search(query=query, collection=tool_call["name"])
        response = llm(query=query, context=context, chat_history=chat_history)
        response = list(response)
        response[1] = response[1] + initial_tokens
        return JSONResponse(content=response, status_code=200)
    
    else:
        return ["As a Legal Assistant, my role is to provide information and guidance on legal matters.\n\nTo answer your question, I would need to provide information outside of my designated scope. Instead, I would like to inform you to ask a question relevant to a legal context, such as contract law, intellectual property, or any other legal topic. I'll be happy to assist you with that. \n\nPlease ask a question related to law, and I'll do my best to provide a helpful response.",initial_tokens]