# app.py
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from embedding_manager import EmbeddingManager


# Define a class for the request
class TextRequest(BaseModel):
    text: str


# Initialize FastAPI
app = FastAPI()

embedding_manager = EmbeddingManager()


# Endpoint
@app.post("/generate_embedding/")
async def generate_embedding(request: TextRequest) -> List[float]:
    text = request.text
    embedding = embedding_manager.generate_embedding(text)
    return embedding
