# Text Embedding Service with FastAPI and Docker

This project implements a **FastAPI** web service that provides an endpoint for generating text embeddings using the `all-MiniLM-L6-v2` model from **SentenceTransformers**. The application is containerized with Docker and supports CUDA acceleration.

## Project Structure

### 1. `embedding_manager.py`
This module defines the `EmbeddingManager` class:
- Loads the `all-MiniLM-L6-v2` model from `sentence-transformers`.
- Exposes the method `generate_embedding(text: str) -> List[float]` which takes text and returns its embedding vector.
- Handles empty input by returning an empty list.


### 2. `app.py`
This file defines the **FastAPI** application:
- Defines the request model `TextRequest` (based on `pydantic`) with a single `text: str` field.
- Initializes FastAPI and the `EmbeddingManager`.
- Exposes a **POST** endpoint at `/generate_embedding/` that receives text and returns the embedding as a list of floats.

Example usage:
```bash
curl -X POST "http://localhost:8000/generate_embedding/" \
     -H "Content-Type: application/json" \
     -d '{"text": "This is an example"}'
```
### 3. `Dockerfile`
Defines the Docker image:
- Based on **CUDA 11.7 with cuDNN 8 on Ubuntu 20.04** (`nvidia/cuda:11.7.1-cudnn8-runtime-ubuntu20.04`).
- Installs Python dependencies.
- Copies application code into `/app`.
- Installs packages listed in `requirements.txt`.
- Exposes port `8000`.
- Runs the app with Uvicorn:
```
uvicorn app:app --host 0.0.0.0 --port 8000
```

## Build the Docker Image
From the project root (where the `Dockerfile` is located):
```
docker build -t embeddings-service .
```

## Run the Container
Run the service with GPU support:
```docker run --gpus all -p 8000:8000 embeddings-service```
The API will be available at:
http://localhost:8000

Interactive documentation (Swagger UI) can be accessed at:
http://localhost:8000/docs

## Running Tests
Run the tests:
```pytest -v test_app.py```
The tests will:
- Build the Docker image.
- Start the container.
- Verify the API works as expected.
- Ensure the embedding output from the API matches the direct Python version.

## Notes

- NVIDIA drivers and nvidia-docker2 are required for GPU acceleration