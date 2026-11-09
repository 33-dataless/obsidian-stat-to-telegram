from os import getenv
from dotenv import load_dotenv
from datetime import datetime
from pathlib import Path
import logging

def configure_logger() -> None:
    logging.basicConfig(level=logging.INFO)

class Config:
    BASE_DIR = Path(__file__).resolve().parent
    load_dotenv(BASE_DIR / ".env")
    _OBSIDIAN_PATH = getenv("PATH_OBSIDIAN")
    _BASE64_KEY = getenv("BASE64_KEY")
config = Config

def get_current_time():
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

