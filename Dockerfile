# Image officielle Python
FROM python:3.11-slim

# Dossier de travail dans le conteneur
WORKDIR /app

# Mise à jour de pip pour éviter des problèmes de compatibilité et de hash
RUN pip install --upgrade pip

# Copier requirements et installer les dépendances
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le projet dans le conteneur
COPY . .

# Exposer le port (Render détecte automatiquement mais on le garde pour Docker Compose)
EXPOSE 8000

# Commande de démarrage FastAPI avec variable d'environnement PORT (par défaut à 8000)
CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port $PORT --reload"]

