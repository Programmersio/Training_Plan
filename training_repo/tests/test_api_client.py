import sys
import os
import pytest
import httpx
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from python_examples.api_client import ApiClient

@pytest.mark.asyncio
async def test_get_success(monkeypatch):
    """Test ApiClient.get returns JSON on 200 OK."""
    class MockResponse:
        def __init__(self):
            self.status_code = 200
        def raise_for_status(self):
            pass
        def json(self):
            return {"ok": True}
    class MockClient:
        async def __aenter__(self): return self
        async def __aexit__(self, exc_type, exc, tb): pass
        async def get(self, *args, **kwargs): return MockResponse()
    monkeypatch.setattr(httpx, "AsyncClient", lambda *a, **k: MockClient())
    client = ApiClient("http://test")
    result = await client.get("/test")
    assert result == {"ok": True}

@pytest.mark.asyncio
async def test_post_success(monkeypatch):
    """Test ApiClient.post returns JSON on 200 OK."""
    class MockResponse:
        def __init__(self):
            self.status_code = 200
        def raise_for_status(self):
            pass
        def json(self):
            return {"posted": True}
    class MockClient:
        async def __aenter__(self): return self
        async def __aexit__(self, exc_type, exc, tb): pass
        async def post(self, *args, **kwargs): return MockResponse()
    monkeypatch.setattr(httpx, "AsyncClient", lambda *a, **k: MockClient())
    client = ApiClient("http://test")
    result = await client.post("/test", data={"foo": "bar"})
    assert result == {"posted": True}
