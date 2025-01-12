# Use uma imagem oficial do Python como base
FROM python:3.10-slim

# Atualize e instale dependências do sistema
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Defina o diretório de trabalho
WORKDIR /lulu_teaches

# Copie os arquivos do projeto
COPY . /lulu_teaches

# Instale as dependências do Python
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Rodar collectstatic antes de iniciar a aplicação
RUN python manage.py collectstatic --noinput

# Exponha a porta 8080 (usada pelo Cloud Run)
EXPOSE 8080

CMD ["gunicorn", "mvp.wsgi:application", "--bind", "0.0.0.0:8080"]