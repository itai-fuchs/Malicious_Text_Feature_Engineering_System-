# Use official Python slim image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Prevent Python from buffering logs
ENV PYTHONUNBUFFERED=1

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app folder
COPY app ./app



CMD ["python", "app/main.py"]
