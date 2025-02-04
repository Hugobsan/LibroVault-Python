from app.core.model import model_instance

def generate_embedding(text: str):
    return model_instance.encode(text)
