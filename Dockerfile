# Použijme lehký image s Pythonem
FROM python:3.11-slim

# Nastavení proměnných
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Nainstaluj systémové závislosti
RUN apt-get update && apt-get install -y build-essential curl && \
    pip install --upgrade pip

# Instaluj Poetry
RUN curl -sSL https://install.python-poetry.org | python3 - && \
    ln -s /root/.local/bin/poetry /usr/local/bin/poetry

# Pracovní adresář
WORKDIR /app

# Zkopíruj project
COPY pyproject.toml poetry.lock* /app/

# Instalace závislostí bez virtuálního prostředí
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

# Zbytek aplikace
COPY . /app

# Vytvoř potřebné složky
RUN mkdir -p ./images ./config_files

# Port FastAPI serveru
EXPOSE 8000

# Spuštění aplikace
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
