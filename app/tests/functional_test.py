import pytest
import pytest_asyncio
from app.services.swapi_client import SWAPIClient


@pytest_asyncio.fixture
async def swapi_client():
    client = SWAPIClient()
    yield client
    await client.close()


@pytest.mark.asyncio
async def test_fetch(monkeypatch):
    client = SWAPIClient()

    class MockResponse:
        def raise_for_status(self):
            pass

        def json(self):
            return {"results": [{"title": "A New Hope"}]}

    async def mock_get(url):
        return MockResponse()

    monkeypatch.setattr("httpx.AsyncClient.get", mock_get)
    result = await client.fetch("films/")
    assert result == [{"title": "A New Hope"}]
