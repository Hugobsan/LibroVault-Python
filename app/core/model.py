import os
from sentence_transformers import SentenceTransformer
from app.core.config import config
class Model:
    def __init__(self):
        print(f"🔄 Loading model: {config.MODEL_NAME}")
        self.model = SentenceTransformer(config.MODEL_NAME)
        self.normalize = config.needs_normalization()
        print(f"🔄 Normalization Required: {self.normalize}")

    def encode(self, text):
        embedding = self.model.encode(text).tolist()
        return self.normalize_embedding(embedding) if self.normalize else embedding

    def normalize_embedding(self, embedding):
        """ Normaliza o embedding para magnitude 1, se necessário """
        import numpy as np
        norm = np.linalg.norm(embedding)
        return (embedding / norm).tolist() if norm > 0 else embedding

model_instance = Model()
