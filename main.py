from fastapi import FastAPI
from app.api import embedding, search
from app.core.config import config

app = FastAPI(title="Semantic API")

app.include_router(embedding.router, prefix="/api")
app.include_router(search.router, prefix="/api")

if __name__ == "__main__":
    import hypercorn.asyncio
    from hypercorn.config import Config as HypercornConfig

    hypercorn_config = HypercornConfig()
    hypercorn_config.bind = [f"{config.API_HOST}:{config.API_PORT}"]
    
    import asyncio
    asyncio.run(hypercorn.asyncio.serve(app, hypercorn_config))
