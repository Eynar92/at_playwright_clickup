"""Module to manage loggers"""
import logging
import colorlog

class CustomLogger(logging.Logger):
    """Class to manage a custom logger

    Parameters
    ----------
    logging: ob
        logging object
    """

    def __init__(self, name: str):
        """Initialize logger

        Parameters
        ----------
        name: str
            Context where logger runs
        """
        super().__init__(name)
        self.configure()

    def configure(self):
        """Configure handlers, set levels, and formatters"""
        log_format = "%(log_color)s[%(asctime)s] [%(levelname)s] [%(name)s] =>>> %(reset)s %(message)s"
        log_colors = {
            "DEBUG": "cyan",
            "INFO": "green",
            "WARNING": "yellow",
            "ERROR": "red",
            "CRITICAL": "red,bg_white",
        }

        formatter = colorlog.ColoredFormatter(
            log_format, datefmt="%d-%b-%y %H:%M:%S", log_colors=log_colors, reset=True
        )

        # Console handler (for colore output)
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        console_handler.setFormatter(formatter)

        # File handler (no colors, but logs everything)
        file_formatter = logging.Formatter(
            "[%(asctime)s] [%(levelname)s] [%(name)s] =>>> %(message)s",
            datefmt="%d-%b-%y %H:%M:%S",
        )
        file_handler = logging.FileHandler("file.log")
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(file_formatter)

        # Adding handlers
        self.addHandler(console_handler)
        self.addHandler(file_handler)

    def close(self):
        """Close and flush all handlers."""
        for handler in self.handlers:
            handler.flush()
            handler.close()
            self.removeHandler(handler)
