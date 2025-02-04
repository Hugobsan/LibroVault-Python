from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Dict
import json
import numpy as np
from app.services.search_service import search

router = APIRouter()

class SearchRequest(BaseModel):
    query: str
    embeddings: List[Dict[str, str]]  # Lista de dicionários com 'book_id', 'page_number', 'embedding' (caminho do arquivo JSON)

@router.post("/embedding/compare")
async def search_embeddings(data: SearchRequest):
    # Criar embedding da consulta
    from app.services.embedding_service import generate_embedding
    query_embedding = generate_embedding(data.query)

    # Carregar embeddings dos arquivos informados
    document_embeddings = []
    metadata = []

    for emb in data.embeddings:
        try:
            with open(emb["embedding"], "r") as f:
                embedding_data = json.load(f)
                document_embeddings.append(embedding_data["embedding"])
                metadata.append({
                    "page_number": emb["page_number"],
                    "book_id": emb["book_id"],
                    "embedding": emb["embedding"]
                })
        except Exception as e:
            print(f"Erro ao carregar o embedding {emb['embedding']}: {e}")

    # Se não houver embeddings carregados, retorna um ranking vazio
    if not document_embeddings:
        return {"ranking": []}

    # Executar busca semântica
    results = search(query_embedding, document_embeddings, top_k=10)

    # Mapear os resultados de volta aos metadados
    ranking = [
        {
            "page_number": metadata[hit["corpus_id"]]["page_number"],
            "book_id": metadata[hit["corpus_id"]]["book_id"],
            "embedding": metadata[hit["corpus_id"]]["embedding"],
            "similarity": hit["score"]
        }
        for hit in results
    ]

    return {"ranking": ranking}
