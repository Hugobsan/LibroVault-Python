from fastapi import APIRouter
from pydantic import BaseModel
from app.services.embedding_service import generate_embedding

router = APIRouter()

class EmbeddingRequest(BaseModel):
    text: str
    book_id: int
    page_number: int

@router.post("/embedding/make")
async def create_embedding(data: EmbeddingRequest):
    embedding = generate_embedding(data.text)

    return {
        "embedding": embedding
    }