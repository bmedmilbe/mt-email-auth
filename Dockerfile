# Use the official Python 3.10 slim image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Install pipenv and system dependencies for psycopg2/pillow
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    python3-dev \
    libjpeg-dev \
    zlib1g-dev \
    && pip install --no-cache-dir pipenv

# Copy Pipfile and Pipfile.lock
COPY Pipfile Pipfile.lock /app/

# Install dependencies using --system to avoid creating a second virtualenv
RUN pipenv install --deploy --system

# Copy the rest of the project
COPY . /app/

# Expose port 8000
EXPOSE 8000

# Start command (Make sure to replace camaramz with your actual project name)
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "camaramz.wsgi:application"]