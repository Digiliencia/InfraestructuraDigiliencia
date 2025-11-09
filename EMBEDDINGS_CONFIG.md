# Configuración de Embeddings

Este proyecto soporta dos proveedores de embeddings:

## 1. API Custom (FastAPI Service)

Usa el microservicio FastAPI local con sentence-transformers.

### Configuración en `.env`:

```env
EMBEDDINGS_PROVIDER=custom
EMBEDDINGS_SERVICE=http://localhost:8000/embed
EMBEDDINGS_MODEL=sentence-transformers/all-MiniLM-L6-v2
EMBEDDINGS_DIMENSION=384
```

### Iniciar el servicio:

```bash
cd services/embeddings
python main.py
```

El servicio estará disponible en `http://localhost:8000/embed`

## 2. Ollama

Usa Ollama para generar embeddings con modelos locales.

### Configuración en `.env`:

```env
EMBEDDINGS_PROVIDER=ollama
EMBEDDINGS_SERVICE=http://localhost:11434
EMBEDDINGS_MODEL=Qwen/Qwen3-Embedding-8B
EMBEDDINGS_DIMENSION=1024
```

### Requisitos:

1. Instalar Ollama: https://ollama.ai
2. Descargar el modelo:

```bash
ollama pull Qwen/Qwen3-Embedding-8B
```

### Verificar que Ollama está corriendo:

```bash
# Verificar versión
curl http://localhost:11434/api/version

# Probar embeddings
curl http://localhost:11434/api/embed -d '{
  "model": "Qwen/Qwen3-Embedding-8B",
  "input": "Hello world"
}'
```

## Uso en el Código

El `EmbeddingService` detecta automáticamente el proveedor configurado:

```python
from digiliencia.data.services.embedding_service import EmbeddingService

# Usa la configuración del .env automáticamente
service = EmbeddingService()

# Generar embeddings
texts = ["Hello world", "Another text"]
embeddings = service.generate_embeddings(texts)
```

## Para Llama-Index

El `CustomAPIEmbedding` también soporta ambos proveedores:

```python
from digiliencia.utils.embeddings import CustomAPIEmbedding
from digiliencia.configs.env import env

# Configuración automática desde .env
embed_model = CustomAPIEmbedding(
    api_url=env.embeddings_service,
    provider=env.embeddings_provider,
    model=env.embeddings_model,
    embedding_dimension=env.embeddings_dimension
)
```

## Modelos Recomendados

### Para Ollama:

- `Qwen/Qwen3-Embedding-8B`
- `nomic-embed-text`
- `mxbai-embed-large`

### Para Custom API:

- `sentence-transformers/all-MiniLM-L6-v2`
- `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`
- `BAAI/bge-large-en-v1.5`

## Cambiar entre Proveedores

Solo necesitas cambiar la variable `EMBEDDINGS_PROVIDER` en el `.env`:

```env
# Usar API custom
EMBEDDINGS_PROVIDER=custom
EMBEDDINGS_SERVICE=http://localhost:8000/embed

# O usar Ollama
EMBEDDINGS_PROVIDER=ollama
EMBEDDINGS_SERVICE=http://localhost:11434
```

No es necesario cambiar código, el sistema se adapta automáticamente.
