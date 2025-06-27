# Image officielle Python
FROM python:3.11-slim

# Dossier de travail dans le conteneur
WORKDIR /app

# Copier requirements et installer
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le projet dans le conteneur
COPY . .

# Exposer le port utilisé par FastAPI
EXPOSE 8000

# Commande de démarrage FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
