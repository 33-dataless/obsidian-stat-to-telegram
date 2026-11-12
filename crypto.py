import json
import base64
from nacl.secret import Aead

from event import Event
from config import config

class Crypto:
    def __init__(self):
        self._key = base64.b64decode(config._BASE64_KEY)
        self._cipher = Aead(self._key)

    def encrypt(self, type_event: str, snapshot: dict):
        payload = {
            "event": type_event,
            "snapshot": snapshot
        }
    
        raw = json.dumps(payload).encode("utf-8")
        encrypted = self._cipher.encrypt(raw)
    
        return encrypted