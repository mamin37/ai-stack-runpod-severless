FROM runpod/base:0.4.0-cuda12.1.0

WORKDIR /app

# System deps
RUN apt-get update && apt-get install -y \
    git wget curl && \
    rm -rf /var/lib/apt/lists/*

# Python deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app
COPY . .

CMD ["python", "-u", "handler.py"]