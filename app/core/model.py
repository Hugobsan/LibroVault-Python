import os
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv

load_dotenv()

class Model:
    def __init__(self):
        # Aqui é possível trocar o modelo de embedding
        self.model = SentenceTransformer(os.getenv("MODEL_NAME", "distiluse-base-multilingual-cased"))

    def encode(self, text):
        return self.model.encode(text).tolist()

model_instance = Model()
