# Use an official lightiweight Python image
FROM python:3.9-bullseye

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
RUN mkdir /app

# Install required system packages for matplotlib
RUN apt-get update \
   && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir numpy matplotlib scikit-learn

# Copy your Python script into the container
COPY app.py /app/app.py

# Run your script
ENTRYPOINT ["python3", "/app/app.py"]
