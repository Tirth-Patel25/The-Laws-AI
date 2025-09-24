from pymilvus import MilvusClient, CollectionSchema, FieldSchema, DataType, Collection
from services.extractors import extractor
from services.embedder import generate_embeddings, search_embeddings
from utils.chunker import chunker, create_ids

import time
import os
from dotenv import load_dotenv
from collections import defaultdict

load_dotenv()

schema = CollectionSchema(
    fields=[
        FieldSchema(name="id", dtype=DataType.VARCHAR, is_primary=True, auto_id=False, max_length=20),
        FieldSchema(name="vector", dtype=DataType.FLOAT_VECTOR, dim=768, metric_type="COSINE"),
        FieldSchema(name="text", dtype=DataType.VARCHAR, max_length=65535),
    ],
    description="Collection for storing text embeddings",
)

milvus_client = MilvusClient(uri=os.getenv("MILVUS_URI"), db_name=os.getenv("MILVUS_DB_NAME"))

def create_collection(collection: str) -> dict:
    index_params = milvus_client.prepare_index_params()

    index_params.add_index(
        field_name="vector", 
        index_type="HNSW",
        metric_type="COSINE",
        efConstruction=256,
        M=64
    )

    try:
        milvus_client.create_collection(
            collection_name=collection,
            schema=schema,
            index_params=index_params,
        )
        return {"status": 200, "message": "created"}
    except Exception as e:
        return {"status": 400, "message": str(e)}

def insert(collection: str, file_name: str,  file_type: str, file) -> dict | None:
    chunks = extractor(file=file, type=file_type, category=collection)
    # chunks = chunker(file_content, category=collection)
    print("length of chunks:", len(chunks))
    current_time = time.time()
    embeddings = generate_embeddings(chunks)
    embedding_time = time.time()
    print("Time taken:", embedding_time - current_time)
    print("length of embeddings:", len(embeddings))

    # Check if Collection Exist
    collection_exist = milvus_client.has_collection(collection_name=collection)
    if not collection_exist:
        collection_response = create_collection(collection=collection)

        # Collection Created Successfully?
        if collection_response["status"] != 200:
            return collection_response["message"]

    chunk_ids = create_ids(name=file_name, length=len(chunks))
    data_to_insert = [{"id": chunk_id, "vector": embedding, "text": chunk} for embedding, chunk, chunk_id in zip(embeddings, chunks, chunk_ids)]
    response = milvus_client.insert(
        collection_name=collection,
        data=data_to_insert,
    )
    print("Inserted Data")
    print("Response from Milvus:", response)
    return response if response else None
    # return "Something"

def search(query: str,collection:str) -> str:
    search_query = search_embeddings(query=query)

    search_params = {
        "field_name":"vector", 
        "index_type":"HNSW",
        "metric_type":"COSINE",
        "efConstruction":256,
        "M":64,
        "radius": 0.6
    }
    
    # # Get Documents
    # documents = milvus_client.search(
    #     collection_name=collection, 
    #     data=[search_query], 
    #     search_params=search_params,
    #     filter="not id like '%_@_1'",
    #     limit=5, 
    #     output_fields=["text", "id"]
    # )[0]

    # # Get header chunks
    # header_chunks = milvus_client.search(
    #     collection_name=collection, 
    #     data=[search_query], 
    #     search_params=search_params,
    #     filter="id LIKE '%_@_1'",
    #     limit=5, 
    #     output_fields=["text", "id"]
    # )[0]

    # Actual search
    chunks = milvus_client.search(
        collection_name=collection, 
        data=[search_query], 
        search_params=search_params,
        limit=5, 
        output_fields=["text", "id"]
    )[0]

    # print("Docs: ", documents)
    # if documents and header_chunks:
    if chunks:
        context = ""
        for chunk in chunks:
            print("Context:\n", chunk['id'], chunk['distance'])
            context += f"{chunk['entity']['text']}\n"
        return context
    else:
        return "No Context Found Do not response"
