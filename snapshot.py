
from pathlib import Path
import json


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

        if not self.path.exists():
            raise FileNotFoundError(f"Directory not found: {path}")

        self.parser = Parser(self.path)

    def create_snapshot(self) -> dict:
        snapshot = {}

        for file_path in self.parser.scan_directory():
            char_count = self.parser.get_char_count(file_path)
            snapshot[str(file_path)] = char_count

        return snapshot

    def serialize_snapshot(self) -> str:
        snapshot = self.create_snapshot()

        return json.dumps(
            snapshot,
            ensure_ascii=False,
            indent=4
        )
