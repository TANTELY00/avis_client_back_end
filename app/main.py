from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.models import client, review, sentiment_result
from app.db import engine, Base
from app.api.endpoints import reviews

app = FastAPI()

origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(reviews.router, prefix="/reviews", tags=["reviews"])

# Création des tables
@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

