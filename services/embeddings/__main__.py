from main import app, build_app

if __name__ == "__main__":
    # Ejecutar con: uv run python -m services.embeddings
    # Para desarrollo, preferir: uv run uvicorn services.embeddings.main:app --reload
    import uvicorn

    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
