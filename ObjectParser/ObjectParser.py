import json
import re
import typing
from enum import IntEnum

import requests

from .Guess import Guess
from .Keyword import Keyword
from .Member import Member
from .Method import Method
from .AbaqusObject import AbaqusObject


class BaseDocument:

    def __init__(self):
        self.lines: list[str] = []

    def addLine(self, line: str):
        self.lines.append(line)

    def reset(self):
        self.lines = []

    def isEmpty(self):
        return len(self.lines) == 0

    def toDict(self) -> dict:
        return {'lines': self.lines}


class EmphasizedItemize(BaseDocument):

    def __init__(self):
        super(EmphasizedItemize, self).__init__()
        self.label = ''

    def addLine(self, line: str):
        self.lines.append(line)

    def setLabel(self, label: str):
        self.label = label

    def reset(self):
        super(EmphasizedItemize, self).reset()
        self.label = ''

    def isEmpty(self):
        return super(EmphasizedItemize, self).isEmpty() and self.label == ''

    def toDict(self) -> dict:
        superDict = super(EmphasizedItemize, self).toDict()
        superDict.update({'label': self.label})
        return superDict


class SectionBaseDocument(BaseDocument):

    def __init__(self):
        super(SectionBaseDocument, self).__init__()
        self.itemizes: dict[str, EmphasizedItemize] = {}

    def addEmphasizedItemize(self, emphasizedItemize: EmphasizedItemize, label: str = None):
        if label is None:
            label = emphasizedItemize.label
        self.itemizes[label] = emphasizedItemize

    def reset(self):
        super(SectionBaseDocument, self).reset()
        self.itemizes = {}

    def toDict(self) -> dict:
        superDict = super(SectionBaseDocument, self).toDict()
        superDict.update({'itemizes': {label: itemize.toDict() for label, itemize in self.itemizes.items()}})
        return superDict


class SubSubSection(SectionBaseDocument):

    def __init__(self, subSubHeader: str = ''):
        super(SubSubSection, self).__init__()
        self.subSubHeader = subSubHeader

    def setSubSubHeader(self, subSubHeader: str):
        self.subSubHeader = subSubHeader

    def reset(self):
        super(SubSubSection, self).reset()
        self.subSubHeader = ''

    def isEmpty(self):
        return super(SubSubSection, self).isEmpty() and self.subSubHeader == ''

    def toDict(self) -> dict:
        superDict = super(SubSubSection, self).toDict()
        superDict.update({'subSubHeader': self.subSubHeader})
        return superDict


class SubSection(SectionBaseDocument):

    def __init__(self, subHeader: str = ''):
        super(SubSection, self).__init__()
        self.subHeader = subHeader
        self.subSubSections: dict[str, SubSubSection] = {}

    def addSubSubSection(self, subSubSection: SubSubSection, subSubHeader: str = None):
        if subSubHeader is None:
            subSubHeader = subSubSection.subSubHeader
        self.subSubSections[subSubHeader] = subSubSection

    def setSubHeader(self, subHeader: str):
        self.subHeader = subHeader

    def reset(self):
        super(SubSection, self).reset()
        self.subHeader = ''
        self.subSubSections = {}

    def isEmpty(self):
        return super(SubSection, self).isEmpty() and self.subHeader == '' and len(self.subSubSections) == 0

    def toDict(self) -> dict:
        superDict = super(SubSection, self).toDict()
        superDict.update({'subHeader': self.subHeader,
                          'subSubSections': {subSubHeader: subSubSection.toDict()
                                             for subSubHeader, subSubSection in self.subSubSections.items()}})
        return superDict


class Section(SectionBaseDocument):

    def __init__(self, header: str = ''):
        super(Section, self).__init__()
        self.header = header
        self.subSections: dict[str, SubSection] = {}

    def addSubSection(self, subSection: SubSection, subHeader: str = None):
        if subHeader is None:
            subHeader = subSection.subHeader
        self.subSections[subHeader] = subSection

    def setHeader(self, header: str):
        self.header = header

    def reset(self):
        super(Section, self).reset()
        self.header = ''
        self.subSections = {}

    def isEmpty(self):
        return super(Section, self).isEmpty() and self.header == '' and len(self.subSections) == 0

    def toDict(self) -> dict:
        superDict = super(Section, self).toDict()
        superDict.update({'header': self.header,
                          'subSections': {subHeader: subSection.toDict()
                                          for subHeader, subSection in self.subSections.items()}})
        return superDict


class Document(SectionBaseDocument):

    def __init__(self, text: str = '', filePath: str = None, url: str = None):
        super(Document, self).__init__()
        self.text = text
        if filePath is not None:
            with open(filePath, 'r+') as file:
                self.text = file.read()
        if url is not None:
            self.text = requests.get(url).text

        self.sections: dict[str, Section] = {}
        self.title: str = ''

    def addSection(self, section: Section, header: str = None, title: typing.Union[bool, str] = True):
        if header is None:
            header = section.header
        self.sections[header] = section
        if isinstance(title, bool) and title:
            self.title = header
        elif isinstance(title, str):
            self.title = title

    def reset(self):
        super(Document, self).reset()
        self.sections = {}

    def isEmpty(self):
        return super(Document, self).isEmpty() and self.text == '' and len(self.sections) == 0

    def toDict(self) -> dict:
        superDict = super(Document, self).toDict()
        superDict.update({'sections': {header: section.toDict()
                                       for header, section in self.sections.items()}})
        return superDict

    def toJson(self, filePath: str):
        with open(filePath, 'w+') as file:
            json.dump(self.toDict(), file, indent=4)
            file.close()


class Position(IntEnum):
    Document = 0
    Section = 1
    SubSection = 2
    SubSubSection = 3
    EmphasizedItemize = 4


class ObjectParser:

    def __init__(self, text: str = '', filePath: str = None, url: str = None):
        self.text = text
        if filePath is not None:
            with open(filePath, 'r+', encoding='utf-8') as file:
                self.text = file.read()
        if url is not None:
            self.text = requests.get(url).text

        self.document = Document()

    def toJson(self, filePath: str):
        self.document.toJson(filePath)

    def parse(self):
        self.document.reset()
        position, itemizePosition = Position.Document, Position.Document
        section, subSection, subSubSection, itemize = Section(), SubSection(), SubSubSection(), EmphasizedItemize()

        lines = self.text.split('\n')
        for line in lines:

            if line.lstrip().rstrip() == '' or line.startswith('```'):
                continue

            if line.startswith('#'):
                if not itemize.isEmpty():
                    if itemizePosition == Position.Document:
                        self.document.addEmphasizedItemize(itemize)
                    elif itemizePosition == Position.Section:
                        section.addEmphasizedItemize(itemize)
                    elif itemizePosition == Position.SubSection:
                        subSection.addEmphasizedItemize(itemize)
                    elif itemizePosition == Position.SubSubSection:
                        subSubSection.addEmphasizedItemize(itemize)

            if line.startswith('# '):
                if not subSubSection.isEmpty():
                    subSection.addSubSubSection(subSubSection)
                if not subSection.isEmpty():
                    section.addSubSection(subSection)
                if not section.isEmpty():
                    self.document.addSection(section)
                section, subSection, subSubSection, itemize = Section(), SubSection(), SubSubSection(), EmphasizedItemize()
                section.setHeader(line[2:])
                position = Position.Section

            elif line.startswith('## '):
                if not subSubSection.isEmpty():
                    subSection.addSubSubSection(subSubSection)
                if not subSection.isEmpty():
                    section.addSubSection(subSection)
                subSection, subSubSection, itemize = SubSection(), SubSubSection(), EmphasizedItemize()
                subSection.setSubHeader(line[3:])
                position = Position.SubSection

            elif line.startswith('### '):
                if not subSubSection.isEmpty():
                    subSection.addSubSubSection(subSubSection)
                subSubSection, itemize = SubSubSection(), EmphasizedItemize()
                subSubSection.setSubSubHeader(line[4:])
                position = Position.SubSubSection

            elif line.startswith('- *') and line.endswith('*'):
                if not itemize.isEmpty():
                    if itemizePosition == Position.Document:
                        self.document.addEmphasizedItemize(itemize)
                    elif itemizePosition == Position.Section:
                        section.addEmphasizedItemize(itemize)
                    elif itemizePosition == Position.SubSection:
                        subSection.addEmphasizedItemize(itemize)
                    elif itemizePosition == Position.SubSubSection:
                        subSubSection.addEmphasizedItemize(itemize)

                itemize = EmphasizedItemize()
                itemize.setLabel(line[3:][:-1])
                if not position == Position.EmphasizedItemize:
                    itemizePosition = position
                position = Position.EmphasizedItemize

            elif position == Position.Document:
                self.document.addLine(line)

            elif position == Position.Section:
                section.addLine(line)

            elif position == Position.SubSection:
                subSection.addLine(line)

            elif position == Position.SubSubSection:
                subSubSection.addLine(line)

            elif position == Position.EmphasizedItemize:
                itemize.addLine(line.lstrip().rstrip())

        if not itemize.isEmpty():
            if itemizePosition == Position.Document:
                self.document.addEmphasizedItemize(itemize)
            elif itemizePosition == Position.Section:
                section.addEmphasizedItemize(itemize)
            elif itemizePosition == Position.SubSection:
                subSection.addEmphasizedItemize(itemize)
            elif itemizePosition == Position.SubSubSection:
                subSubSection.addEmphasizedItemize(itemize)

        if not subSubSection.isEmpty():
            subSection.addSubSubSection(subSubSection)

        if not subSection.isEmpty():
            section.addSubSection(subSection)

        if not section.isEmpty():
            self.document.addSection(section)

        return self

    def toAbaqusObject(self) -> AbaqusObject:
        obj = AbaqusObject()
        if self.document.isEmpty():
            self.parse()

        if len(self.document.sections) == 0:
            raise ValueError('Found no object')

        title = self.document.title
        obj.name = title.split()[0]
        obj.Type = title.split()[-1]
        obj.docs = self.document.sections[title].lines
        obj.parent = Guess.guessParent(''.join(obj.docs))
        if 'more information about the {} object'.format(obj.name) in '\n'.join(obj.docs):
            obj.baseDerived = True
            obj.parent = obj.name
            obj.userDefinedTypes.append(obj.name)
        if obj.parent not in obj.userDefinedTypes and not obj.parent == '':
            obj.derived = True
            obj.userDefinedTypes.append(obj.parent)
        for subHeader, subSection in self.document.sections[title].subSections.items():
            if 'Access' in subHeader:
                accesses = []
                wordWrapped = False
                for i in range(len(subSection.lines)):
                    if wordWrapped:
                        wordWrapped = False
                        continue
                    line = subSection.lines[i].lstrip()
                    wordWrapped = False
                    if line.endswith('\\') and i+1 < len(subSection.lines):
                        wordWrapped = True
                        line = line[:-1] + subSection.lines[i + 1].lstrip()
                    accesses.append(line)
                obj.accesses = accesses

            elif 'Members' in subHeader:
                for label, itemize in subSection.itemizes.items():
                    argType, default, userDefinedType = Guess.guessType(''.join(itemize.lines))
                    if userDefinedType is not None:
                        for Type in userDefinedType.split():
                            if Type not in obj.userDefinedTypes and not Type == '' and not Type == obj.name:
                                obj.userDefinedTypes.append(Type)
                    if (('Boolean' in argType or 'SymbolicConstant' in argType) and
                            'from abaqusConstants import *' not in obj.imports):
                        obj.imports.append('from abaqusConstants import *')
                    if 'typing' in argType and 'import typing' not in obj.imports:
                        obj.imports.append('import typing')
                    member = Member(label, argType, default, itemize.lines)
                    obj.members[member.name] = member
            elif 'Corresponding analysis keywords' in subHeader:
                for line in subSection.lines:
                    keyword, link = Guess.parserMarkdownLink(line)
                    obj.keywords[keyword] = Keyword(keyword, link)
            else:
                methodName = re.sub('(\w+).+', '\g<1>', subHeader)
                methodName = '__init__' if obj.name == methodName else methodName
                method = Method(methodName)
                method.docs = subSection.lines
                for subSubHeader, subSubSection in subSection.subSubSections.items():
                    if 'Path' in subSubHeader:
                        method.paths = subSubSection.lines
                    elif 'Required arguments' in subSubHeader or 'Optional arguments' in subSubHeader:
                        required = True if 'Required arguments' in subSubHeader else False

                        if 'Optional arguments' in subSubHeader:
                            simplifiedLines = re.sub(r'\[([\w\s]+)\]\(.+?\)', '\g<1>', '\n'.join(subSubSection.lines))
                            if len(re.findall('The optional arguments to setValues.+ same.+ {}'.format(obj.name),
                                   simplifiedLines)) > 0:
                                excludedStrings = re.findall('except.+ argument', '\n'.join(subSubSection.lines))
                                if len(excludedStrings) > 0:
                                    for arg in obj.methods['__init__'].args:
                                        if arg.required or arg.name in excludedStrings[0]:
                                            continue
                                        method.addOptionalArgument(arg.name, arg.argType, arg.default, arg.docs)
                                continue

                        for label, itemize in subSubSection.itemizes.items():
                            argDocs = itemize.lines
                            argType, default, userDefinedType = Guess.guessType(''.join(argDocs))
                            if userDefinedType is not None and userDefinedType not in obj.userDefinedTypes:
                                for Type in userDefinedType.split():
                                    if Type not in obj.userDefinedTypes and not Type == '' and not Type == obj.name:
                                        obj.userDefinedTypes.append(Type)
                            if (('Boolean' in argType or 'SymbolicConstant' in argType) and
                                    'from abaqusConstants import *' not in obj.imports):
                                obj.imports.append('from abaqusConstants import *')
                            if 'typing' in argType and 'import typing' not in obj.imports:
                                obj.imports.append('import typing')
                            method.addArgument(label, argType, required, default, argDocs)

                    elif 'Table data' in subSubHeader:
                        obj.tableData = subSubSection.lines

                    elif 'Return value' in subSubHeader:
                        method.returnDocs = subSubSection.lines
                    elif 'Exceptions' in subSubHeader:
                        method.exceptions = subSubSection.lines
                obj.methods[method.name] = method

        return obj
