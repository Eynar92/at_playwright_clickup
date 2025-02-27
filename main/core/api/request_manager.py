"""Module to manage the requests to an API"""
from typing import Dict, Any, Optional
import requests
from main.core.utils.custom_logger import CustomLogger
from main.core.utils.json_reader import JsonReader
from main.core.error_handling.error_handler_factory import ErrorHandlerFactory
from main.core.api.http_methods_enum import HttpMethods

LOGGER = CustomLogger(__name__)


class RequestManager:
    """Handles API requests using configuration files."""

    _instance = None
    _initialized = False

    def __new__(cls):
        """Override __new__ to ensure singleton behavior."""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        """Initializes the instance configuration."""
        if not self._initialized:
            self.config = JsonReader.get_json("configuration.json")
            self.env_name = self.config.get("environment", "test")
            self.environment = JsonReader.get_json(
                "environment.json").get(self.env_name, {})
            self.base_url = self.environment.get("api-url", "")
            self.headers = {
                "Content-Type": self.environment.get("headers", "application/json")}
            RequestManager._initialized = True

    @classmethod
    def get_instance(cls):
        """Returns the singleton instance."""
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def send_request(self,
                     method: HttpMethods,
                     endpoint: str,
                     **kwargs: Optional[Dict[str, Any]]) -> requests.Response:
        """Sends an HTTP request and returns the response.

        Parameters
        ----------
        method: HttpMethods
            HTTP method.
        endpoint: str
            API endpoint to request.
        params: dict, optional
            Query parameters for GET requests.
        data: dict, optional
            Data payload for POST/PUT requests.
        headers: dict, optional
            Custom headers to override defaults.
        Returns
        -------
        requests.Response
            The response object.
        """
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        request_headers = {**self.headers, **kwargs.get('headers' or {})}

        LOGGER.info(f"Sending {method.value} request to {url}")
        try:
            response = requests.request(
                method=method.value,
                url=url,
                params=kwargs.get('params'),
                json=kwargs.get('data'),
                headers=request_headers,
                timeout=10
            )
            response.raise_for_status()
            return response
        except Exception as err:
            handler = ErrorHandlerFactory.get_error_handler(err)
            handler.handle(err)
