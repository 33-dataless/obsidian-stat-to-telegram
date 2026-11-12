import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

def configure_logger() -> None:
    log_dir = Path("./client-logs")

    log_format = ("~ [ %(asctime)s | %(levelname)-8s | %(name)s | %(message)s ]")
    formatter = logging.Formatter(
        fmr=log_format,
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    file_handler = RotatingFileHandler(
        filename=dir / "main.log",
        maxBytes=5*1024*1024,
        backupCount=5,
        encoding="utf-8"
    )

    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)

    root_logger.handlers.clear()

    root_logger.addHandler(console_handler)
    root_logger.addHandler(file_handler)   