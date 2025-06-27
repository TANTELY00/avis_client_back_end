from transformers import pipeline

# Pipeline sentiment
sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

# Pipeline text-generation pour theme et suggestion
generation_pipeline = pipeline("text2text-generation", model="google/flan-t5-small")

async def analyze_sentiment(text: str) -> str:
    result = sentiment_pipeline(text)
    label = result[0]['label']
    return label

def generate_theme(text: str) -> str:
    prompt = f"Generate a short theme for this review: '{text}'"
    response = generation_pipeline(prompt, max_length=20, do_sample=True)
    theme = response[0]['generated_text']
    return theme.strip()

def generate_suggestion(text: str) -> str:
    prompt = f"Based on this review, suggest an improvement or reply: '{text}'"
    response = generation_pipeline(prompt, max_length=40, do_sample=True)
    suggestion = response[0]['generated_text']
    return suggestion.strip()
