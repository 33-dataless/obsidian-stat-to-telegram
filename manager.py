from scanner import Scanner
from snapshot import SnapshotManager
from planner import Planner
from crypto import Crypto

class Manager:
    def __init__(self, path):
        self.path = path

        # SCANER
        self.scanner = Scanner(
            path=self.path,
            recursive=True
        )

        self.observer = self.scanner.registrate_observer()
        self.observer.start()

        # PLANNER
        self.planner = Planner()

        # SNAPSHOT
        self.snapshot_manager = SnapshotManager(self.path)

        # CRYPTO
        self.crypto = Crypto()

    def start(self):
        pass