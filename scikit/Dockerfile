# Use an official Python image
FROM python:3.9-bullseye

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies
RUN apt-get update \
    && rm -rf /var/lib/apt/lists/*

# Install dependencies
RUN pip install --no-cache-dir scikit-learn

# Create the /app directory
RUN mkdir /app

# Copy your script
COPY app.py /app/app.py

# Run the script
ENTRYPOINT ["python3", "/app/app.py"]
