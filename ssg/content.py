import re
from yaml import load,FullLoader
from collections.abc import Mapping

class Content(Mapping):
    __delimiter = "^(?:-|\+){3}\s*$"
    __regex = re.compile(__delimiter, re.MULTILINE)

    def load(self, cls, string):
        _, fm, content = cls.__regex.split(2)
        metadata = load(fm, load=FullLoader)
        return cls(metadata, content)

    def __init__(self,metadata,content):
        self.data = metadata
        self.[content] =  content
