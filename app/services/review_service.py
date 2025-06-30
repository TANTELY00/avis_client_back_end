from app.models.review import Review
from app.models.sentiment_result import SentimentResult
from app.models.client import Client
from app.services.nlp import analyze_sentiment, generate_theme, generate_suggestion
from sqlalchemy import select


async def create_review(db, text: str, client_name: str, client_email: str):
    # Vérifie si le client existe déjà
    existing_client = await db.execute(
        select(Client).where(Client.email == client_email)
    )
    client = existing_client.scalars().first()

    # Sinon, crée le client
    if not client:
        client = Client(name=client_name, email=client_email)
        db.add(client)
        await db.commit()
        await db.refresh(client)

    # Crée le review lié à ce client
    new_review = Review(text=text, client_id=client.id)
    db.add(new_review)
    await db.commit()
    await db.refresh(new_review)

    # Analyse du sentiment et autres
    sentiment = await analyze_sentiment(text)
    theme = generate_theme(text)
    suggestion = generate_suggestion(text)

    result = SentimentResult(review_id=new_review.id, sentiment=sentiment, theme=theme, suggestion=suggestion)
    db.add(result)
    await db.commit()

    return {
        "review_id": new_review.id,
        "client_id": client.id,
        "sentiment": sentiment,
        "theme": theme,
        "suggestion": suggestion
    }
