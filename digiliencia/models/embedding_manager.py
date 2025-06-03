from sentence_transformers import SentenceTransformer
from typing import List


class EmbeddingManager:
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def generate_embedding(self, text: str) -> List[float]:
        if not text.strip():
            return []
        embedding = self.model.encode(text, show_progress_bar=False)
        return embedding.tolist()


# call the function
if __name__ == "__main__":
    embedding_manager = EmbeddingManager()
    text = "This is a sample text for generating embeddings."
    embedding = embedding_manager.generate_embedding(text)
    print(embedding)
