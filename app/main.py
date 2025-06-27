from fastapi import FastAPI
from app.api.endpoints import reviews
from app.db import engine, Base

app = FastAPI()

app.include_router(reviews.router)

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        # Création des tables
        await conn.run_sync(Base.metadata.create_all)
