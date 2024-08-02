# Dockerfile
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Install psycopg2 (PostgreSQL adapter for Python)
RUN pip install psycopg2-binary

# Copy project
COPY . /app/

# Create a directory for static files
RUN mkdir -p /app/staticfiles

# Collect static files
RUN python manage.py collectstatic --noinput

EXPOSE 8000

# Create a script to run migrations and start the server
RUN echo '#!/bin/sh\n\
python manage.py migrate\n\
gunicorn --bind 0.0.0.0:8000 portofolio.wsgi:application\n'\
> /app/start.sh && chmod +x /app/start.sh

# Run the script
CMD ["/app/start.sh"]