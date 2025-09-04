from fastapi import FastAPI, HTTPException, Body, Request, File, UploadFile
from fastapi.responses import JSONResponse
from pymilvus import MilvusClient

# Custom Imports
from services.milvus_services import insert, search
from services.llm_response import llm

# Environment config imports
from dotenv import load_dotenv
import os
load_dotenv()

# <----- Milvus ----->
milvus = MilvusClient(host="localhost", port=19530)

# <----- FastAPI ----->
app = FastAPI()

# <----- ENDPOINTS ----->
@app.get("/")
async def root():
    return JSONResponse(content="Hello from The Laws!!!", status_code=200)

# <----- File Upload ----->
@app.post("/upload")
async def ask(category: str, file: UploadFile = File(...)):
    file_name = file.filename
    allowed_extensions = ["pdf", "docx", "doc", "json"]
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
    context = search(query=query)
    response = llm(query=query, context=context)
    return JSONResponse(content=response, status_code=200)
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host=os.getenv("API_HOST"), port=int(os.getenv("API_PORT")), reload=True)