import threading
import json

from scanner import Scanner
from snapshot import SnapshotManager
from crypto import Crypto
from client import Client
from event import Event


class Manager:
    def __init__(self, path, url):
        self.path = path

        self.timer = None
        self.timer_lock = threading.Lock()

        self.debounce_seconds = 20


        self.scanner = Scanner(
            path=self.path,
            callback=self.on_file_changed,
            recursive=True
        )

        self.observer = self.scanner.registrate_observer()

        self.snapshot_manager = SnapshotManager(self.path)
        self.crypto = Crypto()

        self.url = url
        self.client = Client(self.url)

    def on_file_changed(self, event):
        with self.timer_lock:
            if self.timer is not None:
                self.timer.cancel()

            self.timer = threading.Timer(
                self.debounce_seconds,
                self.commit
            )

            self.timer.daemon = True
            self.timer.start()

    def commit(self):
        with self.timer_lock:
            self.timer = None

        current_json = self.snapshot_manager.serialize_snapshot()

        snapshot = json.loads(current_json)

        encrypt_json = self.crypto.encrypt(
            type_event=Event.OBSIDIAN.value,
            snapshot=snapshot
        )

        response_json = self.client.post(encrypt_json)
        print(F"ОТПРАВЛЕН КОММИТ XD : {response_json}")

    def start(self):
        self.observer.start()

    def stop(self):

        self.observer.stop()
        self.observer.join()

        with self.timer_lock:   
            if self.timer is not None:
                self.timer.cancel()
                self.timer = None