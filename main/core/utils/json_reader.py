"""Module to read JSON files"""
import os
import json
from typing import Dict, Any
from main.core.utils.custom_logger import CustomLogger
from main.core.error_handling.error_handler_factory import ErrorHandlerFactory

LOGGER = CustomLogger(__name__)


class JsonReader:
    """JsonReader Implementation
    This class provides methods to read any JSON file and return its content as a dictionary.
    """
    @staticmethod
    def get_json(config_file: str = "/main/core/resources/config_sample.json") -> Dict[str, Any]:
        """Method to get data from a JSON file

        Parameters
        ----------
        config_file: str
            Path to the JSON file

        Returns
        -------
        dict
            Dictionary containing the JSON Data
        """
        location_file = os.path.join(os.getcwd(), config_file.lstrip('/'))
        try:
            with open(location_file) as json_file:
                configuration = json.load(json_file)
        except Exception as err:
            handler = ErrorHandlerFactory.get_error_handler(err)
            handler.handle(err)

        LOGGER.info(f"Successfully read JSON file: \"{config_file}\"")
        return configuration

    def __str__(self) -> str:
        pass
