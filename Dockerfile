# Image officielle Python
FROM python:3.11-slim

# Dossier de travail dans le conteneur
WORKDIR /app

# Copier requirements et installer
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le projet dans le conteneur
COPY . .

# Exposer le port (Render s'en moque mais on le garde pour docker-compose)
EXPOSE 8000

# Commande de démarrage FastAPI avec variable d'environnement PORT
CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000} --reload"]
