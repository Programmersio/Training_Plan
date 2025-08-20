"""
HTTP client class skeleton for training exercises.

This module defines a class ``ApiClient`` that represents a simple HTTP client.
The goal is to practise implementing methods to interact with a REST API using
an AI coding assistant.  The class includes stub methods for common HTTP
operations and leaves implementation details to be filled in.  Use unit tests
and mocking techniques to verify the behaviour.
"""

from typing import Any, Dict, Optional

try:
    import requests
except ImportError:
    requests = None  # type: ignore


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

    def get(self, path: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Send a GET request to the API and return the JSON response.

        The method should build the full URL from ``self.base_url`` and ``path``,
        include ``self.headers`` and query parameters, send the request, check
        the status code and return the parsed JSON content.  If the response
        indicates an error (non‑2xx status), raise an exception with an
        informative message.  Use the ``requests`` library if available.

        Parameters
        ----------
        path : str
            The resource path relative to the base URL (e.g. ``"/users"``).
        params : Dict[str, Any], optional
            Query parameters to include in the request.

        Returns
        -------
        Dict[str, Any]
            The response body parsed from JSON.
        """
        # TODO: implement this method using an AI coding assistant
        raise NotImplementedError

    def post(self, path: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Send a POST request to the API and return the JSON response.

        Build the full URL, include headers and send a POST request with a
        JSON body derived from ``data``.  Handle errors similarly to the GET
        method and return the parsed response.  Consider adding basic retry
        logic if the request fails due to transient network errors.

        Parameters
        ----------
        path : str
            The resource path relative to the base URL (e.g. ``"/users"``).
        data : Dict[str, Any], optional
            A dictionary representing the JSON body of the request.

        Returns
        -------
        Dict[str, Any]
            The response body parsed from JSON.
        """
        # TODO: implement this method using an AI coding assistant
        raise NotImplementedError