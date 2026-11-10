from scanner import Scanner
from snapshot import SnapshotManager
from planner import Planner
from crypto import Crypto
from client import Client

class Manager:
    def __init__(self, path, url):
        self.path = path

        # SCANNER
        self.scanner = Scanner(
            path=self.path,
            recursive=True
        )

        self.observer = self.scanner.registrate_observer()
        # self.observer.start()

        # PLANNER
        self.planner = Planner()

        # SNAPSHOT
        self.snapshot_manager = SnapshotManager(self.path)

        # CRYPTO
        self.crypto = Crypto()

        # CLIENT 
        self.url = url
        self.client = Client(self.url)

    def go(self):
        # detect changes in obsidian

        # planner

        pass