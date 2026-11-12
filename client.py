import httpx
from config import config

class Client:
    def __init__(self, url):
        self._url = url

    def post(self, encrypted):
        response = httpx.post(
            self._url,
            content=bytes(encrypted),
            headers={
                "Authorization": config._BASE64_KEY,
            },
            trust_env=False
        )
        response.raise_for_status()
        return response.json()
    