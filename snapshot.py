from pathlib import Path
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
        number_word = len(content)
        return number_word
    
class Snapshot:
    def __init__(self, path: str):
        if Path.exists(path):
            self.path = Path(path)
            self.parser = Parser(self.path)
        self.current_snapshot = {}
                
    def create_snapshot(self):
        if not self.current_snapshot:
            '''первое создание снапшота'''
            for elem in list(self.parser.scan_directory()):
                nubmer_word = self.parser.get_number_char_in_file(Path(elem))
                self.current_snapshot[elem] = nubmer_word
        
        
        return self.current_snapshot

class SnapshotStorage:
    def __init__(self):
        self.path = Path(r"\logs")
        
        




    
                



        