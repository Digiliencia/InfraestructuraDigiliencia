import pytest
from httpx import AsyncClient

pytestmark = pytest.mark.asyncio


async def test_health_endpoint(api_client: AsyncClient):
    """Health endpoint should return 200 and a small JSON payload."""
    response = await api_client.get("http://127.0.0.1:8000/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
