from app.services.nlp import analyze_sentiment

def generate_theme(text: str) -> str:
    return "Thème automatique"

def generate_suggestion(text: str) -> str:
    return "Voici une suggestion basée sur votre avis."

analyze_sentiment = analyze_sentiment
