from app.models.review import Review
from app.models.sentiment_result import SentimentResult
from app.services.nlp import analyze_sentiment

async def create_review(db, text):
    new_review = Review(text=text)
    db.add(new_review)
    await db.commit()
    await db.refresh(new_review)

    sentiment = await analyze_sentiment(text)

    result = SentimentResult(review_id=new_review.id, sentiment=sentiment)
    db.add(result)
    await db.commit()

    return {"review_id": new_review.id, "sentiment": sentiment}
