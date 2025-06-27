from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base


from app.core.config import DATABASE_URL

engine = create_async_engine(DATABASE_URL, echo=True)


engine = create_async_engine(DATABASE_URL, echo=True)
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

Base = declarative_base()

async def get_async_session():
    async with async_session() as session:
        yield session
