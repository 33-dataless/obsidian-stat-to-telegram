from os import getenv
from dotenv import load_dotenv
from pathlib import Path
import logging

def configure_logger() -> None:
    logging.basicConfig(level=logging.INFO)
    
def get_path():
    BASE_DIR = Path(__file__).resolve().parent
    load_dotenv(BASE_DIR / ".env")

    path = getenv("PATH_OBSIDIAN")

    if not path:
        raise ValueError("PATH_OBSIDIAN not found in .env")

    return Path(path)