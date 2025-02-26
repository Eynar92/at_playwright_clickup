"""Module for handling various types of exceptions."""
from abc import ABC, abstractmethod
import json
import requests
from main.core.utils.custom_logger import CustomLogger

LOGGER = CustomLogger(__name__)

class ErrorHandlerStrategy(ABC):
    """Abstract base class for error handling strategies.
    This class defines the interface that all concrete error handler strategies must implement
    """
    @abstractmethod
    def handle(self, exception: BaseException) -> None:
        """Handle the given exepction

        Parameters
        ----------
        excepction: BaseException
            The exception to handle.
        """
        pass

class FileNotFoundErrorHandlerstrategy(ErrorHandlerStrategy):
    """Strategy for handling FileNotFoundError exceptions.
    This strategy logs the error and re-raises the exception.
    """
    def handle(self, exception: FileNotFoundError) -> None:
        """Handle FileNotFoundError exceptions.
        Parameters
        ----------
        exception: FileNotFoundError
            The FileNotFoundError exception to handle.
        """
        LOGGER.error(f"File not found: {exception}")
        raise exception

class JSONDecoderErrorHandlerStrategy(ErrorHandlerStrategy):
    """Strategy for handling JSONDecoderError exceptions.
    This strategy logs the error and re-raises the exception.
    """
    def handle(self, exception: json.JSONDecodeError) -> None:
        """Handle JSONDecodeError exceptions.
        Parameters
        ----------
        exception: JSONDecodeError
            The JSONDecodeError exception to handle.
        """
        LOGGER.error(f"Error decoding JSON: {exception}")
        raise exception

class RequestTimeoutErrorHandlerStrategy(ErrorHandlerStrategy):
    """Strategy for handling requests.Timeout exceptions.
    This strategy logs the error and re-raises the exception.
    """
    def handle(self, exception: requests.Timeout) -> None:
        """Handle requests.Timeout exceptions.
        Parameters
        ----------
        exception: requests.Timeout
            The Timeout exception to handle.
        """
        LOGGER.error(f"Request timeout: {exception}")
        raise exception

class HTTPErrorHandlerStrategy(ErrorHandlerStrategy):
    """
    Strategy for handling requests.HTTPError exceptions.
    This strategy logs the error and re-raises the exception.
    """
    def handle(self, exception: requests.HTTPError) -> None:
        """
        Handle requests.HTTPError exceptions.
        Parameters
        ----------
        exception: requests.HTTPError
            The HTTPError exception to handle.
        """
        LOGGER.error(f"HTTP error. {exception.response.status_code} - {exception.response.text}")
        raise exception

class RequestExceptionHandlerStrategy(ErrorHandlerStrategy):
    """
    Strategy for handling requests.RequestException exceptions.
    This strategy logs the error and re-raises the exception.
    """
    def handle(self, exception: requests.RequestException) -> None:
        """
        Handle requests.RequestException exceptions.
        Parameters
        ----------
        exception: requests.RequestException
            The RequestException exception to handle.
        """
        LOGGER.error(f"Request error: {exception}")
        raise exception

class GeneralErrorHandlerStrategy(ErrorHandlerStrategy):
    """
    Strategy for handling general exceptions.
    
    This strategy logs the error and re-raises the exception.
    """
    def handle(self, exception: BaseException) -> None:
        """
        Handle general exceptions.
        
        Parameters
        ----------
        exception: BaseException
            The exception to handle.
        """
        LOGGER.error(f"Unexpected error: {exception}")
        raise exception
