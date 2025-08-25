# test_app.py
import subprocess
import time
import requests
import pytest
import numpy as np

from embedding_manager import EmbeddingManager

IMAGE_NAME = "embeddings-service"
CONTAINER_NAME = "embeddings-test-container"
API_URL = "http://localhost:8000/generate_embedding/"


@pytest.fixture(scope="session", autouse=True)
def run_container():
    """
    Build and run the Docker container before tests,
    then stop and remove it afterwards.
    """
    # Build the Docker image
    subprocess.run(["docker", "build", "-t", IMAGE_NAME, "."], check=True)

    # Run the container
    subprocess.Popen(
        [
            "docker",
            "run",
            "--rm",
            "--gpus",
            "all",
            "--name",
            CONTAINER_NAME,
            "-p",
            "8000:8000",
            IMAGE_NAME,
        ]
    )

    # Wait until the API is ready
    for _ in range(30):  # 30 * 2s = 60 seconds timeout
        try:
            r = requests.get("http://localhost:8000/docs")
            if r.status_code == 200:
                break
        except Exception:
            pass
        time.sleep(2)
    else:
        # Timeout
        subprocess.run(["docker", "logs", CONTAINER_NAME])
        subprocess.run(["docker", "stop", CONTAINER_NAME])
        raise RuntimeError("API did not start in time")

    yield

    # Teardown: stop container
    subprocess.run(["docker", "stop", CONTAINER_NAME])


def test_connection():
    """
    Simple test: check that the embedding endpoint responds correctly.
    """
    response = requests.post(API_URL, json={"text": "ping"})
    assert response.status_code == 200
    embedding = response.json()
    assert isinstance(embedding, list)
    assert all(isinstance(x, float) for x in embedding)


def test_embedding_api_vs_direct():
    text = "This is a test sentence for embeddings."

    # Direct embedding
    manager = EmbeddingManager()
    direct_embedding = manager.generate_embedding(text)

    # API embedding
    response = requests.post(API_URL, json={"text": text})
    assert response.status_code == 200
    api_embedding = response.json()

    # Convert to numpy for comparison
    direct_arr = np.array(direct_embedding, dtype=float)
    api_arr = np.array(api_embedding, dtype=float)

    # Assert same shape
    assert direct_arr.shape == api_arr.shape

    # Assert vectors are close (floating point tolerance)
    np.testing.assert_allclose(direct_arr, api_arr, rtol=1e-5, atol=1e-5)
