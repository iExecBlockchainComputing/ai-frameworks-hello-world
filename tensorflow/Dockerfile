FROM python:3.9-bullseye

# Set non-interactive frontend for apt
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies
RUN apt-get update \
    && rm -rf /var/lib/apt/lists/*

# Install tensorflow
RUN pip install --upgrade pip
RUN pip install --no-cache-dir tensorflow

# Create the /app directory
RUN mkdir /app

# Copy your script into the /app directory
COPY app.py /app/app.py

# Run the script
ENTRYPOINT ["python3", "/app/app.py"]
