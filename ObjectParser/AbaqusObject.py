import os
import re

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
        self.parentArgTypeHints: str = ''
        self.tableData: list[str] = []
        self.parent: str = ''
        self.accesses: list[str] = []
        self.methods: list[Method] = []
        self.members: dict[str, Member] = {}
        self.keywords: dict[str, Keyword] = {}

        self.imports: list[str] = []
        self.userDefinedTypes: list[str] = []

        self.script = ''

    def findMethodsByName(self, name: str):
        methods = []
        for method in self.methods:
            if method.name == name:
                methods.append(method)
        return methods

    def splitDocs(self, sep: str = ' ', maxLength: int = 90):
        splitDocs = []
        for doc in self.docs:
            splitDocs += Method.splitText(Guess.removeMarkdownLinks(doc), sep, maxLength)
        return splitDocs

    def methodOverloadedIndexes(self):
        overload: list = len(self.methods) * [0]
        if len(self.methods) == 0:
            return []
        currentMethodName = ''
        currentNum = 1
        for method, index in zip(self.methods, range(len(self.methods))):
            if method.name == currentMethodName:
                overload[index-1] = currentNum
                currentNum += 1
                overload[index] = currentNum
            else:
                currentNum = 1
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

    def generateUserDefinedTypeImport(self, userDefinedType: str, fileDir: str, foundDir: str):
        relPath = os.path.relpath(foundDir, fileDir)

        if relPath == '.':
            importString = 'from .{} import {}'.format(userDefinedType, userDefinedType)
        else:
            nParentLevels = max(len(re.findall(r"\W\\", relPath)), len(re.findall(r"\W/", relPath)))
            folders = relPath[nParentLevels * 3:].split('\\')
            jointFolders = '.'.join(folders)
            importPath = '.' * (nParentLevels + 1) + jointFolders + '.{}'.format(userDefinedType)
            importString = 'from {} import {}'.format(importPath, userDefinedType)
        if userDefinedType == self.name and self.baseDerived:
            importString += ' as Base{}'.format(self.name)
        self.imports.append(importString)

    def searchImports(self, fileDir: str = 'abaqus', searchDir: str = None):
        if searchDir is not None:
            for userDefinedType in self.userDefinedTypes:

                foundDir, foundFile = AbaqusObject.findUserDefinedType(userDefinedType, fileDir)
                if foundDir == '' or foundFile == '' and searchDir is not None:
                    foundDir, foundFile = AbaqusObject.findUserDefinedType(userDefinedType, searchDir)

                if foundDir == '' or foundFile == '':
                    if userDefinedType.endswith('Array'):
                        baseType = userDefinedType[:-5]
                        foundBaseTypeDir, foundBaseTypeFile = AbaqusObject.findUserDefinedType(baseType, 'abaqus')
                        if foundBaseTypeDir is None or foundBaseTypeFile is None:
                            print('        {} not existed'.format(baseType))
                            continue

                        text = 'from .{} import {}\n\n\n'.format(baseType, baseType)
                        text += 'class {}(list[{}]):\n'.format(userDefinedType, baseType)
                        text += '    def findAt(self):\n'
                        text += '        pass\n'

                        with open(os.path.join(foundBaseTypeDir, userDefinedType + '.py'), 'w+', encoding='utf-8') as f:
                            f.write(text)
                            f.close()

                        self.generateUserDefinedTypeImport(userDefinedType, fileDir, foundBaseTypeDir)
                else:
                    self.generateUserDefinedTypeImport(userDefinedType, fileDir, foundDir)

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
        overloadedIndexes = self.methodOverloadedIndexes()
        if not len(self.methods) == 0:
            for method, index in zip(self.methods, range(len(self.methods))):
                self.script += method.methodString(4, overloadedIndexes[index] > 0, self.derived, self.parentArgTypeHints)
                if overloadedIndexes[index] > 0:
                    if not self.script.lstrip().startswith('import typing'):
                        self.script = 'import typing\n\n' + self.script

                if ((index > 0 and overloadedIndexes[index] > overloadedIndexes[index - 1]) and
                        ((index < len(self.methods) - 1 and overloadedIndexes[index] > overloadedIndexes[index + 1]) or
                         index == len(self.methods) - 1)):
                    self.script += method.overloadMethodString()
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
