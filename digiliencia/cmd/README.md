## Directorio `digiliencia/cmd`

Este directorio contiene scripts de línea de comandos usados para el flujo ETL y clasificación de noticias en el proyecto `InfraestructuraDiligencia`.

Cada script está pensado para ejecutarse como un script independiente desde el entorno del proyecto (por ejemplo, usando `python <script>.py`), y muchos asumen que la conexión a la base de datos (neomodel) y las variables de entorno están configuradas.

### Archivos y para qué sirven

- `chunk_and_embed_news.py`

  - Genera chunks (segmentos) de las noticias existentes y —si se requiere— crea embeddings para los mismos.
  - Parámetros principales (hardcoded en el script o leídos desde `env`): `chunk_size`, `overlap`, `batch_size`.
  - Uso típico: crear chunks faltantes para noticias y prepararlas para recuperación por RAG.

- `classify_unfielded_news.py`

  - Busca noticias sin relaciones a "fields" (campos relacionados) y utiliza `FieldClassificationService` para clasificarlas y crear las relaciones correspondientes en la base de datos.
  - Itera las noticias sin campos y establece relaciones si se encuentran campos.

- `classify_unlabeled_news.py`

  - Similar al anterior, pero clasifica noticias que no tienen `topics` (temas) usando `TopicClassificationService` y las enlaza.

- `embedd_unembedded_news.py`

  - Dos pasos principales:
    1. Crea chunks para noticias que aún no tienen chunks.
    2. Genera embeddings para los chunks que no tienen embedding.
  - Usa `env.em` para determinar el modelo de embeddings a utilizar.
  - Este script es útil para procesar lotes grandes: primero asegura que todos los textos están divididos y luego calcula embeddings en batch.

- `scrap.py`
  - Ejecuta los scrapers configurados (p. ej. `CanadianScraper`, `WEForumScraper`, `IncibeScraper`, `Ncsc`, `AmericaCyberAgencyScraper`, `Nist`) y procesa las noticias raspadas:
    - Valida los datos raspados.
    - Crea la noticia en la BDD mediante `NewsService`.
    - Clasifica la noticia en `topics` y `fields` usando los servicios de clasificación.
    - Genera chunks y embeddings para la noticia creada.
  - Función pública: `scrap(from_days_ago: int = 5)` — por defecto raspa noticias de los últimos 5 días.

### Requisitos previos

- Configurar variables de entorno y conexión a la base de datos. Los scripts llaman a: `digiliencia.configs.env.Env()` o `env` y a `configure_neomodel()` para inicializar la conexión con Neo4j/neomodel.
- Dependencias del proyecto (ver `requirements.txt` o `pyproject.toml`).
- Acceso a los servicios de clasificación y embeddings configurados en `digiliencia/data/services/neomodel/`.

### Ejemplos de uso (PowerShell en Windows)

# 1) Crear chunks faltantes para todas las noticias (usa `env.news_chunk_size` y `env.news_chunk_overlap`):

```powershell
cd c:\Users\alpri\Documents\Github\InfraestructuraDiligencia
python digiliencia\cmd\chunk_and_embed_news.py
```

# 2) Clasificar noticias sin campos (fields):

```powershell
python digiliencia\cmd\classify_unfielded_news.py
```

# 3) Clasificar noticias sin temas (topics):

```powershell
python digiliencia\cmd\classify_unlabeled_news.py
```

# 4) Crear chunks y generar embeddings para noticias que no los tienen:

```powershell
python digiliencia\cmd\embedd_unembedded_news.py
```

# 5) Ejecutar el scraper (ejecuta todo el flujo: scrap -> crear noticia -> clasificar -> chunk & embed):

```powershell
python digiliencia\cmd\scrap.py
```

> Nota: los scripts registran información y errores con `loguru`. Revisa los logs para detectar problemas durante la ejecución.

### Secuencia recomendada para procesar noticias nuevas

1. `scrap.py` —> si quieres importar noticias desde las fuentes públicas y procesarlas automáticamente.
2. `classify_unlabeled_news.py` y `classify_unfielded_news.py` —> si tienes noticias ya en la base y faltan relaciones a topics/fields.
3. `chunk_and_embed_news.py` o `embedd_unembedded_news.py` —> para asegurar que todos los textos están segmentados y embebidos para uso en RAG o búsquedas semánticas.

### Variables/ajustes importantes

- `env.news_chunk_size` y `env.news_chunk_overlap` — afectan cómo se generan los chunks.
- `env.em` — nombre del modelo de embeddings usado por los scripts que generan embeddings.
- `batch_size` y parámetros `limit` en los métodos de `NewsService` — controlan el tamaño de los lotes y la cantidad de registros procesados por ejecución.

### Consejos y resolución de problemas

- Si los scripts lanzan excepciones relacionadas con la base de datos, asegúrate de que `configure_neomodel()` está apuntando a una instancia de Neo4j accesible y que las credenciales están en las variables de entorno.
- Para debugging, ejecuta cada script con pequeños `limit`/`batch_size` (si expones estos parámetros) o modifica temporalmente las constantes en el script para procesar menos registros.
- Revisa `logs/` para encontrar trazas completas si `loguru` escribe ahí.
