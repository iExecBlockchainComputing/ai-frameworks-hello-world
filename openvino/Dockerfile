FROM python:3.9-bullseye

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive

# Install dependencies
RUN apt-get update && apt-get install -y \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install \
    matplotlib \
    numpy \
    ipywidgets \
    openvino-dev \
    scikit-learn \
    opencv-python-headless \
    tqdm

# Create and set the working directory
RUN mkdir -p /app

# Download the model utilities script
RUN wget https://raw.githubusercontent.com/openvinotoolkit/openvino_notebooks/main/notebooks/utils/notebook_utils.py -O /app/notebook_utils.py

# Copy your application files into the container
COPY . /app

# Set the entrypoint for your script
ENTRYPOINT ["python3", "/app/app.py"]
