FROM python:3.9-bullseye

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies
RUN apt-get update \
    && rm -rf /var/lib/apt/lists/*

# Set work directory
RUN mkdir /app

# Copy files
COPY app.py /app/app.py

# Install Python dependencies
RUN pip install --no-cache-dir torch torchvision

# Run the app
ENTRYPOINT ["python3", "/app/app.py"]
