from transformers import pipeline
import asyncio

sentiment_pipeline = pipeline("sentiment-analysis")

async def analyze_sentiment(text: str) -> str:
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, sentiment_pipeline, text)
    return result[0]["label"]
