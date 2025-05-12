# Utiliser une image légère de Python
FROM python:3.9-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers du projet dans le conteneur
COPY . /app

# Installer les dépendances
RUN pip install --no-cache-dir psycopg2-binary python-dotenv flask joblib numpy pandas scikit-learn keras tensorflow

# Exposer le port 5001
EXPOSE 5003

# Lancer l'application
CMD ["python", "server.py"]
