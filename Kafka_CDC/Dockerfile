FROM python:3.9-slim

WORKDIR /app

# Install system dependencies required for psycopg2
RUN apt-get update && \
    apt-get install -y \
    libpq-dev \
    python3-dev \
    gcc && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/consumer.py .

CMD ["python", "consumer.py"]