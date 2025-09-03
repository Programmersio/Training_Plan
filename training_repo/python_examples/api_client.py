"""
HTTP client class skeleton for training exercises.

This module defines a class ``ApiClient`` that represents a simple HTTP client.
The goal is to practise implementing methods to interact with a REST API using
an AI coding assistant.  The class includes stub methods for common HTTP
operations and leaves implementation details to be filled in.  Use unit tests
and mocking techniques to verify the behaviour.
"""


from typing import Any, Dict, Optional
import httpx



class ApiClient:
    """A simple API client for interacting with a REST service.

    The client stores a base URL and optional authentication headers.  It
    provides methods to send GET and POST requests and handles JSON
    serialisation.  To use this class, instantiate it with the base API
    endpoint and then call ``get`` or ``post`` with the appropriate
    resource path and parameters.

    Attributes
    ----------
    base_url : str
        The base URL of the API (e.g. ``"https://api.example.com/v1"``).
    headers : Dict[str, str]
        Optional HTTP headers to include with each request (e.g. for
        authentication).
    timeout : float
        Request timeout in seconds.
    """

    def __init__(self, base_url: str, headers: Optional[Dict[str, str]] = None, timeout: float = 10.0) -> None:
        self.base_url = base_url.rstrip('/')
        self.headers = headers or {}
        self.timeout = timeout

    # Use httpx to send an asynchronous GET request to the path appended to base_url. Include optional headers and query parameters. Raise for non‑2xx responses and return the parsed JSON.
    async def get(self, path: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        url = f"{self.base_url}/{path.lstrip('/')}"
        try:
            response = await httpx.get(url, headers=self.headers, params=params, timeout=self.timeout)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as e:
            # Handle HTTP errors (e.g. 4xx, 5xx)
            print(f"Error fetching {url}: {e}")
            raise

    # Use httpx to send an asynchronous POST request with a JSON body to the path appended to base_url. Include optional headers. Raise on error and return the JSON response.
    async def post(self, path: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        url = f"{self.base_url}/{path.lstrip('/')}"
        try:
            response = await httpx.post(url, headers=self.headers, json=data, timeout=self.timeout)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as e:
            # Handle HTTP errors (e.g. 4xx, 5xx)
            print(f"Error posting to {url}: {e}")
            raise
