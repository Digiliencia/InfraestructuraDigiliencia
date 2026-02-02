# Use a PyTorch image prebuilt with the desired CUDA version
# Or use the nvidia/cuda devel image if you need to compile stuff
FROM pytorch/pytorch:2.7.0-cuda12.8-cudnn9-runtime

# Alternatively, if using NVIDIA’s base:
# FROM nvidia/cuda:12.6.0-cudnn8-runtime-ubuntu22.04

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y \
    python3-pip \
    python3-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN python3 -m pip install --upgrade pip

# Copy the requirements file first (for caching)
COPY requirements.txt /app/requirements.txt

# Install Python dependencies (excluding torch if already in base image)
RUN pip install -r requirements.txt

# If you need a specific version of torch (if base image doesn't already include it)
# RUN pip install torch==2.0.1+cu126 torchvision==0.15.2+cu126 --index-url https://download.pytorch.org/whl/cu126

# Copy the rest of the application
COPY . /app

# Expose port
EXPOSE 8000

# Entrypoint / command
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
