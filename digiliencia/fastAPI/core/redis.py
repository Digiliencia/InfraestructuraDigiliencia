# core/redis.py
import redis.asyncio as redis
from core.config import settings

redis_pool = redis.ConnectionPool.from_url(
    f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}/0", decode_responses=True
)


async def get_redis():
    """
    Dependencia de FastAPI para obtener una conexión a Redis.
    """
    client = redis.Redis.from_pool(redis_pool)
    try:
        yield client
    finally:
        await client.aclose()
