# test_app.py
import requests
import numpy as np
import sys
import os

embedding_manager_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../digiliencia/models")
)
sys.path.append(embedding_manager_path)
from embedding_manager import EmbeddingManager

API_URL = "http://localhost:8000/generate_embedding/"


def test_connection(run_container):
    """
    Simple test: check that the embedding endpoint responds correctly.
    """
    response = requests.post(API_URL, json={"text": "ping"})
    assert response.status_code == 200
    embedding = response.json()
    assert isinstance(embedding, list)
    assert all(isinstance(x, float) for x in embedding)


def test_embedding_api_vs_direct(run_container):
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
