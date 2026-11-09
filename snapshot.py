from pathlib import Path
from config import get_current_time
import shutil
import json 
# import re

class Parser:
    def __init__(self, path):
        self.path = path

    def scan_directory(self):
        files = self.path.rglob("*.md")
        return files

    # def clean_file(self, content: str):
    #     content = re.sub(r"^#{1,6}\s+", "", content, flags=re.MULTILINE)
    #     content = re.sub(r"\*\*(.*?)\*\*", r"\1", content)
    #     content = re.sub(r"\*(.*?)\*", r"\1", content)
    #     content = re.sub(r"__(.*?)__", r"\1", content)
    #     content = re.sub(r"_(.*?)_", r"\1", content)
    #     content = re.sub(r"~~(.*?)~~", r"\1", content)
    #     content = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", content)
    #     content = re.sub(r"!\[([^\]]*)\]\([^)]+\)", "", content)
    #     content = re.sub(r"```.*?```", "", content, flags=re.DOTALL)
    #     content = re.sub(r"`[^`]*`", "", content)
    #     content = re.sub(r"^\s*[-*+]\s+", "", content, flags=re.MULTILINE)
    #     content = re.sub(r"^\s*\d+\.\s+", "", content, flags=re.MULTILINE)
    #     content = re.sub(r"\|", " ", content)
    #     content = re.sub(r"[\[\]]", "", content)
    #     return content
        
    def get_number_char_in_file(self, file_path):
        # content = self.clean_file(file_path.read_text(encoding="utf=8"))
        content = file_path.read_text(encoding="utf-8")
        number_chars = len(content)
        return number_chars
               
class SnapshotStorage:
    def __init__(self):
        self.__logs_path__ = Path(r"\logs")
        
    def move_snapshot_to_log(self):
        current_file = Path("current_snapshot.json")
        logs_path = Path("logs")

        logs_path.mkdir(exist_ok=True)

        current_time = get_current_time()

        log_file = logs_path / f"snapshot_log_{current_time}.json"

        shutil.move(str(current_file), str(log_file))

    def dump_snapshot_to_json(self, __current_snapshot__):
        with open("current_snapshot.json", "a", encoding="utf-8") as file:
            json.dump(__current_snapshot__, file, ensure_ascii=False)
 
class Snapshot:
    def __init__(self, path: str):
        if Path(path).exists():
            self.path = Path(path)
            self.parser = Parser(self.path)
            self.snapshot_storage = SnapshotStorage()
        
        self.__current_snapshot__ = {}
        

    def create_snapshot(self):
        for elem in self.parser.scan_directory():
            nubmer_word = self.parser.get_number_char_in_file(Path(elem))
            self.__current_snapshot__[str(elem)] = nubmer_word

    def current_snapshot_is_null(self):
        with open("current_snapshot.json", "r", encoding="utf-8") as file:
            try:
                data = json.load(file)
            except json.decoder.JSONDecodeError:
                return True
            
        if not data:
            return True
        else:
            return False
    
    def snapshot(self):
        current_file = Path("current_snapshot.json")

        if current_file.exists():
                if not self.current_snapshot_is_null():
                    self.snapshot_storage.move_snapshot_to_log()

        self.__current_snapshot__ = {}
        self.create_snapshot()
        self.snapshot_storage.dump_snapshot_to_json(self.__current_snapshot__)
