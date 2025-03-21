import logging

# import logging.config
import os
import traceback
import json_logging
import sys


def setup_logging(app_name="app"):
    """Sets up logging configuration."""

    log_level = os.getenv("LOG_LEVEL", "WARNING").upper()

    logging_config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "json": {
                "()": "json_logging.JSONFormatter",
                "json_ensure_ascii": False,
                "json_indent": None,
                "rename_fields": {"levelname": "severity"},
                "static_fields": {
                    "timestamp": "%(asctime)s",
                    "user": "unknown_user",  # Placeholder
                    "application": app_name,
                },
            },
        },
        "handlers": {
            "file": {
                "class": "logging.handlers.RotatingFileHandler",
                "filename": "log.json",
                "maxBytes": 2048,
                "backupCount": 5,
                "formatter": "json",
                "level": log_level,
            },
        },
        "loggers": {
            "": {
                "handlers": ["file"],
                "level": log_level,
                "propagate": True,
            },
        },
    }

    logging.config.dictConfig(logging_config)
    # json_logging.init_non_web()


def get_logger(name):
    """Returns a logger with the given name."""
    return logging.getLogger(name)


def exception_hook(exc_type, exc_value, tb):
    """Exception hook to log unhandled exceptions."""
    logger = get_logger("exception")
    logger.critical(
        "Unhandled exception",
        extra={
            "exception": {
                "type": exc_type.__name__,
                "value": str(exc_value),
                "traceback": "".join(traceback.format_tb(tb)),
            }
        },
    )

    os._exit(1)  # Exit the application after logging the exception


# Set up exception hook
sys.excepthook = exception_hook


# Dynamically set the user
def set_user(user_id):
    """sets the user for all log messages"""
    logging.getLogger().handlers[0].formatter.defaults["static_fields"][
        "user"
    ] = user_id
