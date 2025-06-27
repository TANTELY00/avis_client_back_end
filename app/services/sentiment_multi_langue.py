from transformers import pipeline

# Pipeline sentiment multilingue
sentiment_pipeline = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

# Pipeline text2text-generation multilingue
generation_pipeline = pipeline("text2text-generation", model="google/mt5-small")

async def analyze_sentiment(text: str) -> str:
    result = sentiment_pipeline(text)
    label = result[0]['label']
    return label

def generate_theme(text: str) -> str:
    prompt = f"Génère un thème court pour cet avis : '{text}'"
    response = generation_pipeline(prompt, max_length=20, do_sample=True)
    theme = response[0]['generated_text']
    return theme.strip()

def generate_suggestion(text: str) -> str:
    prompt = f"Formule une suggestion ou réponse à cet avis : '{text}'"
    response = generation_pipeline(prompt, max_length=50, do_sample=True)
    suggestion = response[0]['generated_text']
    return suggestion.strip()
