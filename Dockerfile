FROM python:3.11-slim

# Avoids creating .pyc files
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# system deps for pillow or sqlite if needed
RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential libsqlite3-dev gcc \
    && rm -rf /var/lib/apt/lists/*

# Install python deps
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . /app

# Expose port
EXPOSE 5000

# Default environment vars
ENV PORT=5000
ENV FLASK_DEBUG=0

# Start with gunicorn
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
