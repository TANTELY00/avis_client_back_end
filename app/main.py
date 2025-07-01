from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.endpoints import reviews
from app.db import engine, Base
from app.models import client, review, sentiment_result

app = FastAPI()

# configuration CORS 
origins = [
    "http://localhost:5173",  # pour le développement local
    "https://avis-client-frontend.onrender.com"  #  frontend Render 
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,        # autorise uniquement ce domaine
    allow_credentials=True,
    allow_methods=["*"],          # autorise toutes les méthodes (GET, POST, OPTIONS...)
    allow_headers=["*"],          # autorise tous les headers
)

app.include_router(reviews.router)

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        # Création des tables
        await conn.run_sync(Base.metadata.create_all)
