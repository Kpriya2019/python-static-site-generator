from typing import List, Any
from pathlib import Path
import shutil

class Parser:
    extensions: List[Any] = []
    
    def valid_extension(self, extension):
        return extension in self.extensions

    def parse(self, source: Path, dest: Path):
        raise NotImplementedError

    def read(self, path):
        with open(path, 'r') as file:
            return file.read()

    def copy(self, path, source, dest):
        shutil.copy2(path, dest/path.relative_to(source))

    def write(self,path,dest,content,ext=".html"):
        full_path = self.dest / path.with_suffix(ext).name
        with open(full_path,'w') as file:
            file.write(content)

class ResourceParser:

    extensions = [".jpg", ".png", ".gif", ".css", ".html"]

    def parser(self, path, source, dest):
        self.copy(path, source, dest)