"""Module for creating and managing error handler strategies."""
import json
from typing import Type, Dict
from .error_handler_strategy import (
    ErrorHandlerStrategy,
    FileNotFoundErrorHandlerstrategy,
    JSONDecoderErrorHandlerStrategy,
    GeneralErrorHandlerStrategy
)


class ErrorHandlerFactory:
    """A factory class to retrieve appropiate error handlers based on exceptions types."""
    _handlers : Dict[Type[BaseException], ErrorHandlerStrategy]= {
        FileNotFoundError: FileNotFoundErrorHandlerstrategy(),
        json.JSONDecodeError: JSONDecoderErrorHandlerStrategy()
    }

    @classmethod
    def get_error_handler(cls, exception: BaseException) -> ErrorHandlerStrategy:
        """
        Retrieve the appropriate error handler for a given exception.

        Parameters
        ----------
        exception: BaseException
            The exception for which an error handler is needed.

        Returns
        -------
        ErrorHandlerStrategy
            The error handler strategy for the given exception type.
        """
        return cls._handlers.get(type(exception), GeneralErrorHandlerStrategy())
