"""Module to manage loggers"""
import logging
from colorlog import ColoredFormatter

class CustomLogger(logging.Logger):
    """Class to manage a custom logger

    Parameters
    ----------
    logging: ob
        logging object
    """
    handlers = []

    def __init__(self, name):
        """Initialize logger

        Parameters
        ----------
        name: context
            context where logger runs
        """
        logging.Logger.__init__(self, name)
        self.configure()

    def close(self):
        """Method to close and flush all the handlers
        """
        for handler in self.handlers:
            handler.flush()
            handler.close()

    def configure(self):
        """Method to configure handlers, set level and set formatters
        """
        log_format = "%(log_color)s [%(asctime)s] [%(levelname)s] [%(name)s] =>>> %(reset)s %(message)s"
        formatter = ColoredFormatter(log_format, datefmt="%d-%b-%y %H:%M:%S")
        console_handler = logging.StreamHandler()
        file_handler = logging.FileHandler("file.log")
        console_handler.setLevel(logging.DEBUG)
        file_handler.setLevel(logging.DEBUG)
        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)
        self.handlers = self.handlers + [console_handler, file_handler]
