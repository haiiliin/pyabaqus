import re

from .Method import Method


class Member:

    def __init__(self, name: str, argType: str = '', default=None, docs: list[str] = None):
        if docs is None:
            docs = []
        self.name = name
        self.argType = argType
        self.default = default
        self.docs = docs

    def splitDocs(self, sep: str = ' ', maxLength: int = 90):
        splitDocs = []
        for doc in self.docs:
            links = re.findall(r'\[\w+\]\(.+?\)', doc)
            if len(links) > 0:
                doc = re.sub(r'\[(\w+)\]\(.+?\)', '\g<1>', doc)
            splitDocs += Method.splitText(doc, sep, maxLength)
        return splitDocs

    def simplifiedDocs(self):
        simplifiedDocs = []
        for doc in self.docs:
            links = re.findall(r'\[\w+\]\(.+?\)', doc)
            if len(links) > 0:
                doc = re.sub(r'\[(\w+)\]\(.+?\)', '\g<1>', doc)
                simplifiedDocs.append(doc)
        return simplifiedDocs

