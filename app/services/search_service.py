import numpy as np
from sentence_transformers.util import semantic_search

def search(query_embedding, document_embeddings, top_k=10):
    """
    Realiza uma busca semântica comparando um embedding de consulta com uma lista de embeddings de documentos.
    """
    document_embeddings = np.array(document_embeddings)
    hits = semantic_search(np.array([query_embedding]), document_embeddings, top_k=top_k)[0]
    return hits
