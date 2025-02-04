import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    API_HOST = os.getenv("API_HOST", "127.0.0.1")
    API_PORT = int(os.getenv("API_PORT", 5000))
    MODEL_NAME = os.getenv("MODEL_NAME", "all-MiniLM-L6-v2")

    MODELS_REQUIRING_NORMALIZATION = {
        "distiluse-base-multilingual-cased": True,
        "distiluse-base-multilingual-cased-v2": True,
        "paraphrase-multilingual-MiniLM-L12-v2": True,
        "all-MiniLM-L6-v2": False,
        "all-mpnet-base-v2": False,
        "all-mpnet-base-v2-v2": False,
    }

    def needs_normalization(self):
        return self.MODELS_REQUIRING_NORMALIZATION.get(self.MODEL_NAME, False)

config = Config()