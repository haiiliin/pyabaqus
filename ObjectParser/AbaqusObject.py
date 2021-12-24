import os
import re

from . import ObjectParser
from .Guess import Guess
from .Keyword import Keyword
from .Member import Member
from .Method import Method


class AbaqusObject:

    def __init__(self):
        self.name: str = ''
        self.Type: str = 'object'
        self.docs: list[str] = []
        self.derived: bool = False
        self.baseDerived: bool = False
        self.parentFilePath: str = ''
        self.tableData: list[str] = []
        self.parent: str = ''
        self.accesses: list[str] = []
        self.methods: dict[str, Method] = {}
        self.members: dict[str, Member] = {}
        self.keywords: dict[str, Keyword] = {}

        self.imports: list[str] = []
        self.userDefinedTypes: list[str] = []

        self.script = ''

    def splitDocs(self, sep: str = ' ', maxLength: int = 90):
        splitDocs = []
        for doc in self.docs:
            splitDocs += Method.splitText(Guess.removeMarkdownLinks(doc), sep, maxLength)
        return splitDocs

    def overloadMethodIndexes(self):
        overload: list = len(self.methods) * [0]
        if len(self.methods) == 0:
            return []
        currentMethodName = ''
        currentNum = 0
        for method, index in zip(self.methods.values(), range(len(self.methods))):
            if method.name == currentMethodName:
                currentNum += 1
                overload[index] = currentNum
            else:
                currentNum = 0
                currentMethodName = method.name
        return overload

    def toPythonScript(self, fileDir: str = None, searchDir: str = None):
        return self.generate(fileDir, searchDir)

    @staticmethod
    def findUserDefinedType(userDefinedType: str, searchDir: str):
        if not os.path.isdir(searchDir):
            raise IOError('{} is not a dir'.format(searchDir))

        files = os.listdir(searchDir)
        for file in files:

            if os.path.isdir(os.path.join(searchDir, file)):
                foundDir, foundFile = AbaqusObject.findUserDefinedType(userDefinedType, os.path.join(searchDir, file))
                if not foundDir == '' and not foundFile == '':
                    return foundDir, foundFile
            elif os.path.isfile(os.path.join(searchDir, file)) and file.endswith('.py'):
                with open(os.path.join(searchDir, file), 'r+', encoding='utf-8') as f:
                    text = f.read()
                    if 'class {}:'.format(userDefinedType) in text or (
                            'class {}('.format(userDefinedType) in text and
                            'class {}(Base{}):'.format(userDefinedType, userDefinedType) not in text
                    ):
                        return searchDir, file.split('.')[0]
                    f.close()
        return '', ''

    def searchImports(self, fileDir: str = 'abaqus', searchDir: str = None):
        if searchDir is not None:
            for userDefinedType in self.userDefinedTypes:

                foundDir, foundFile = AbaqusObject.findUserDefinedType(userDefinedType, fileDir)
                if foundDir == '' or foundFile == '' and searchDir is not None:
                    foundDir, foundFile = AbaqusObject.findUserDefinedType(userDefinedType, searchDir)

                if foundDir == '' or foundFile == '':
                    continue

                relPath = os.path.relpath(foundDir, fileDir)

                if relPath == '.':
                    importString = 'from .{} import {}'.format(userDefinedType, userDefinedType)
                else:
                    nParentLevels = max(len(re.findall(r"\W\\", relPath)), len(re.findall(r"\W/", relPath)))
                    folders = relPath[nParentLevels*3:].split('\\')
                    jointFolders = '.'.join(folders)
                    importPath = '.' * (nParentLevels + 1) + jointFolders + '.{}'.format(userDefinedType)
                    importString = 'from {} import {}'.format(importPath, userDefinedType)
                if userDefinedType == self.name and self.baseDerived:
                    importString += ' as Base{}'.format(self.name)
                self.imports.append(importString)

    def deClass(self):
        self.script = re.sub(r'\n\n+', r'\n\n', self.script)
        if self.Type == 'object' or self.Type == 'Object':
            return self

        lines = self.script.split('\n')
        newLines = []
        for line in lines:
            if line.startswith('    '):
                line = line[4:]
            elif line.startswith('class '):
                continue
            if '(self)' in line:
                line = line.replace('(self)', '()')
            elif '(self,' in line:
                line = line.replace('(self, ', '(')
            newLines.append(line)
        self.script = '\n'.join(newLines)
        self.script = re.sub(r'\n\n+', r'\n\n', self.script)
        return self

    def generateImports(self, fileDir: str = 'abaqus', searchDir: str = None):

        self.searchImports(fileDir, searchDir)
        for ipo in sorted(self.imports):
            self.script += '{}\n'.format(ipo)
        return self

    def generateClassDocStrings(self):
        if self.parent == '':
            self.script += '\n\nclass {}:\n\n'.format(self.name)
        elif self.baseDerived:
            self.script += '\n\nclass {}(Base{}):\n'.format(self.name, self.name)
        else:
            self.script += '\n\nclass {}({}):\n\n'.format(self.name, self.parent)
        docs = self.splitDocs()
        if len(docs) > 0:
            self.script += '    """{}\n'.format(docs[0])
            for i in range(1, len(docs)):
                self.script += '    {}\n'.format(docs[i])
        else:
            self.script += '    """\n'
        self.script += '\n'

        self.script += '    Access\n'
        self.script += '    ------\n'
        for access in self.accesses:
            self.script += '        - {}\n'.format(access)
        self.script += '\n'

        self.script += '    Table Data\n'
        self.script += '    ----------\n'
        for data in self.tableData:
            self.script += '        {}\n'.format(data)
        self.script += '\n'

        self.script += '    Corresponding analysis keywords\n'
        self.script += '    -------------------------------\n'
        for keyword in self.keywords.values():
            self.script += '        - {}\n'.format(keyword.keyword)
        self.script += '\n'

        self.script += '    """\n\n'
        return self

    def generateMembers(self):
        if len(self.members) == 0 and len(self.methods) == 0:
            self.script += '    pass\n'
            return self

        for member in self.members.values():
            docs = member.splitDocs()
            for i in range(len(docs)):
                self.script += '    # {}\n'.format(docs[i])
            if member.argType == self.name:
                self.script += '    {}: \'{}\' = {}\n\n'.format(member.name, member.argType, member.default)
            else:
                self.script += '    {}: {} = {}\n\n'.format(member.name, member.argType, member.default)
        return self

    def generateMethods(self):
        overload = self.overloadMethodIndexes()
        if not len(self.methods) == 0:
            for method, index in zip(self.methods.values(), range(len(self.methods))):
                splitDocs = method.splitDocs()
                argStrings = method.argStringsSplitLists(objectName=self.name)
                if overload[index] > 0:
                    self.script += '    @typing.overload\n'
                    if not self.script.lstrip().startswith('import typing'):
                        self.script = 'import typing\n\n' + self.script

                if len(method.args) == 0:
                    self.script += '    def {}(self):\n'.format(method.name)
                elif len(argStrings) == 1:
                    self.script += '    def {}(self, {}):\n'.format(method.name, argStrings[0])
                else:
                    self.script += '    def {}(self, {}\n'.format(method.name, argStrings[0])
                    for i in range(1, len(argStrings) - 1):
                        self.script += '         ' + ' ' * len(method.name) + '{}\n'.format(argStrings[i])
                    self.script += '         ' + ' ' * len(method.name) + '{}):\n'.format(argStrings[-1])
                self.script += '        """{}\n'.format(splitDocs[0].rstrip())
                for i in range(1, len(splitDocs)):
                    self.script += '        {}\n'.format(splitDocs[i].rstrip())
                self.script += '\n'
                if not len(method.paths) == 0:
                    self.script += '        Path\n'
                    self.script += '        ----\n'
                    for path in method.paths:
                        self.script += '            - {}\n'.format(path)
                    self.script += '\n'
                self.script += '        Parameters\n'
                self.script += '        ----------\n'
                for idx, arg in zip(range(len(method.args)), method.args):
                    self.script += '        {}\n'.format(arg.name)
                    docs = method.splitArgumentDocs(idx)
                    self.script += '            {}\n'.format(docs[0])
                    for i in range(1, len(docs)):
                        self.script += '            {}\n'.format(docs[i])
                self.script += '\n'
                self.script += '        Returns\n'
                self.script += '        -------\n'
                returnsDocs = method.splitReturnDocs()
                if len(returnsDocs) > 0:
                    self.script += '            {}\n'.format(returnsDocs[0])
                    for i in range(1, len(returnsDocs)):
                        self.script += '            {}\n'.format(returnsDocs[i])
                self.script += '\n'
                self.script += '        Exceptions\n'
                self.script += '        ----------\n'
                exceptionsDocs = method.splitExceptionsDocs()
                if len(exceptionsDocs) > 0:
                    self.script += '            {}\n'.format(exceptionsDocs[0])
                    for i in range(1, len(exceptionsDocs)):
                        self.script += '            {}\n'.format(exceptionsDocs[i])
                self.script += '        """\n'
                if method.name == '__init__' and self.derived:
                    if not os.path.exists(self.parentFilePath):
                        self.script += '        super().__init__()\n'
                    else:
                        parentObj = ObjectParser(filePath=self.parentFilePath).parse().toAbaqusObject()
                        argStringsNoTypeHints = parentObj.methods['__init__'].argStringsSplitLists(typeHint=False, objectName=self.name)
                        if len(method.args) == 0:
                            self.script += '        super().__init__()\n'
                        elif len(argStringsNoTypeHints) == 1:
                            self.script += '        super().__init__({})\n'.format(argStringsNoTypeHints[0])
                        else:
                            self.script += '        super().__init__({}\n'.format(argStringsNoTypeHints[0])
                            for i in range(1, len(argStringsNoTypeHints) - 1):
                                self.script += '                 ' + ' ' * len(method.name) + '{}\n'.format(argStringsNoTypeHints[i])
                            self.script += '                 ' + ' ' * len(method.name) + '{})\n'.format(argStringsNoTypeHints[-1])
                self.script += '        pass\n\n'

                if (index > 0 and overload[index] > overload[index - 1]) and ((index < len(self.methods) - 1 and
                                                                               overload[index] > overload[index + 1]) or
                                                                              index == len(self.methods) - 1):
                    requiredArgStrings = method.requiredArgStringsSplitLists()
                    if len(requiredArgStrings) > 0:
                        requiredArgStrings[-1] += ', *args, **kwargs'
                    if len(method.args) == 0:
                        self.script += '    def {}(self):\n'.format(method.name)
                    elif len(requiredArgStrings) == 1:
                        self.script += '    def {}(self, {}):\n'.format(method.name, requiredArgStrings[0])
                    else:
                        self.script += '    def {}(self, {}\n'.format(method.name, requiredArgStrings[0])
                        for i in range(1, len(requiredArgStrings) - 1):
                            self.script += '         ' + ' ' * len(method.name) + '{}\n'.format(requiredArgStrings[i])
                        self.script += '         ' + ' ' * len(method.name) + '{}):\n'.format(requiredArgStrings[-1])
                    self.script += '        pass\n\n'

        return self

    def generate(self, fileDir: str = 'abaqus', searchDir: str = None):
        if not os.path.exists(fileDir):
            try:
                os.makedirs(fileDir)
            except OSError:
                return self

        text = self.generateImports(fileDir, searchDir).generateClassDocStrings().generateMembers().generateMethods().deClass().script
        filepath = os.path.join(fileDir, self.name + '.py')
        with open(filepath, 'w+', encoding='utf-8') as f:
            f.write(text)
            f.close()

        return self
