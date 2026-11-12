
from pathlib import Path
from config import get_current_time
from logging import getLogger
import json

log = getLogger(__name__)

class Parser:
    def __init__(self, path: Path):
        self.path = path

    def scan_directory(self):
        return self.path.rglob("*.md")

    def get_char_count(self, file_path: Path) -> int:
        content = file_path.read_text(encoding="utf-8")
        return len(content)


class SnapshotManager:
    def __init__(self, path: str):
        self.path = Path(path)
        self.path_current_snapshot = Path("./current_snapshot.json")
        self.path_to_log_snapshot = Path("./logs/")

        if not self.path.exists():
            raise FileNotFoundError(f"Directory not found: {path}")

        self.parser = Parser(self.path)

    def create_snapshot(self) -> dict:
        snapshot = {}

        for file_path in self.parser.scan_directory():
            char_count = self.parser.get_char_count(file_path)

            relative_path = file_path.relative_to(self.path)
            snapshot[relative_path.as_posix()] = char_count

        file_log_name = "shapshot_log_" + get_current_time() + ".json"
        path = self.path_current_snapshot
        path.rename(f"{self.path_to_log_snapshot}\\{file_log_name}")
        self.path_current_snapshot.touch()

        with open(self.path_current_snapshot, "w", encoding="utf-8") as file:
            json.dump(snapshot, file, ensure_ascii=False, indent=4)
        log.debug("snapshot created")

        return snapshot

    def serialize_snapshot(self) -> str:
        snapshot = self.create_snapshot()
        
        result = json.dumps(
            snapshot,
            ensure_ascii=False,
            indent=4
        )
        return result
