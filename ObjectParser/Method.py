import re

from .Argument import Argument


class Method:

    def __init__(self, name: str = ''):
        self.name = name
        self.docs: list[str] = []
        self.paths: list[str] = []
        self.args: list[Argument] = []
        self.argNames: list[str] = []
        self.returnDocs: list[str] = []
        self.exceptions: list[str] = []

    def __str__(self):
        return 'name: {}, args: {}'.format(self.name, [str(arg) + ' ' for arg in self.args])

    def reset(self):
        self.name = ''
        self.docs: list[str] = []
        self.paths: list[str] = []
        self.args: list[Argument] = []
        self.argNames = []
        self.returnDocs: list[str] = []
        self.exceptions: list[str] = []

    def addArgument(self, name: str, argType: str = 'str', required: bool = True, default: str = '',
                    docs: list[str] = ''):
        if name in self.argNames or name == '':
            return
        arg = Argument(name, argType, required, default, docs)
        self.argNames.append(name)
        self.args.append(arg)

    def addRequiredArgument(self, name: str, argType: str = 'str', default: str = '', docs: list[str] = ''):
        self.addArgument(name, argType, True, default, docs)

    def addOptionalArgument(self, name: str, argType: str = 'str', default: str = '', docs: list[str] = ''):
        self.addArgument(name, argType, False, default, docs)

    def isEmpty(self):
        return self.name == '' and self.docs == '' and len(self.args) == 0 and self.returnDocs == ''

    def argString(self, index: int, typeHint: bool = True, objectName: str = '') -> str:
        if index < 0 or index >= len(self.args):
            raise ValueError('Index out of range')
        return self.args[index].argString(typeHint, objectName=objectName)

    def overloadMethodString(self):
        text = ''
        requiredArgStrings = self.requiredArgStringsSplitLists()
        if len(requiredArgStrings) > 0:
            requiredArgStrings[-1] += ', *args, **kwargs'
        text += '    def {}(self, *args, **kwargs):\n'.format(self.name)
        # if len(self.args) == 0:
        #     text += '    def {}(self):\n'.format(self.name)
        # elif len(requiredArgStrings) == 1:
        #     text += '    def {}(self, {}):\n'.format(self.name, requiredArgStrings[0])
        # else:
        #     text += '    def {}(self, {}\n'.format(self.name, requiredArgStrings[0])
        #     for i in range(1, len(requiredArgStrings) - 1):
        #         text += '         ' + ' ' * len(self.name) + '{}\n'.format(requiredArgStrings[i])
        #     text += '         ' + ' ' * len(self.name) + '{}):\n'.format(requiredArgStrings[-1])
        text += '        pass\n\n'
        return text

    def methodString(self, indent: int = 4, isOverloaded: bool = False, derived: bool = False,
                     argStringsTypeHints: str = ''):
        text = ''
        splitDocs = self.splitDocs()
        argStrings = self.argStringsSplitLists(objectName=self.name)
        if isOverloaded:
            text += indent * ' ' + '@typing.overload\n'

        if len(self.args) == 0:
            text += indent * ' ' + 'def {}(self):\n'.format(self.name)
        elif len(argStrings) == 1:
            text += indent * ' ' + 'def {}(self, {}):\n'.format(self.name, argStrings[0])
        else:
            text += indent * ' ' + 'def {}(self, {}\n'.format(self.name, argStrings[0])
            for i in range(1, len(argStrings) - 1):
                text += '         ' + ' ' * len(self.name) + '{}\n'.format(argStrings[i])
            text += indent * ' ' + '     ' + ' ' * len(self.name) + '{}):\n'.format(argStrings[-1])
        text += indent * ' ' + '    """{}\n'.format(splitDocs[0].rstrip())
        for i in range(1, len(splitDocs)):
            text += indent * ' ' + '    {}\n'.format(splitDocs[i].rstrip())
        text += '\n'
        if not len(self.paths) == 0:
            text += indent * ' ' + '    Path\n'
            text += indent * ' ' + '    ----\n'
            for path in self.paths:
                text += indent * ' ' + '        - {}\n'.format(path)
            text += '\n'
        text += indent * ' ' + '    Parameters\n'
        text += indent * ' ' + '    ----------\n'
        for idx, arg in zip(range(len(self.args)), self.args):
            text += indent * ' ' + '    {}\n'.format(arg.name)
            docs = self.splitArgumentDocs(idx)
            if len(docs) > 0:
                text += indent * ' ' + '        {}\n'.format(docs[0])
                for i in range(1, len(docs)):
                    text += indent * ' ' + '        {}\n'.format(docs[i])
        text += '\n'
        text += indent * ' ' + '    Returns\n'
        text += indent * ' ' + '    -------\n'
        returnsDocs = self.splitReturnDocs()
        if len(returnsDocs) > 0:
            text += indent * ' ' + '        {}\n'.format(returnsDocs[0])
            for i in range(1, len(returnsDocs)):
                text += indent * ' ' + '        {}\n'.format(returnsDocs[i])
        text += '\n'
        text += indent * ' ' + '    Exceptions\n'
        text += indent * ' ' + '    ----------\n'
        exceptionsDocs = self.splitExceptionsDocs()
        if len(exceptionsDocs) > 0:
            text += indent * ' ' + '        {}\n'.format(exceptionsDocs[0])
            for i in range(1, len(exceptionsDocs)):
                text += indent * ' ' + '        {}\n'.format(exceptionsDocs[i])
        text += indent * ' ' + '    """\n'
        if self.name == '__init__' and derived:
            if argStringsTypeHints == '':
                text += indent * ' ' + '    super().__init__()\n'
            else:
                text += indent * ' ' + '    super().__init__()\n'
                # if len(self.args) == 0:
                #     text += indent * ' ' + '    super().__init__()\n'
                # elif len(argStringsTypeHints) == 1:
                #     text += indent * ' ' + '    super().__init__({})\n'.format(argStringsTypeHints[0])
                # else:
                #     text += indent * ' ' + '    super().__init__({}\n'.format(argStringsTypeHints[0])
                #     for i in range(1, len(argStringsTypeHints) - 1):
                #         text += indent * ' ' + '             ' + ' ' * len(self.name) + '{}\n'.format(
                #             argStringsTypeHints[i])
                #     text += indent * ' ' + '             ' + ' ' * len(self.name) + '{})\n'.format(
                #         argStringsTypeHints[-1])
        text += indent * ' ' + '    pass\n\n'
        return text

    @staticmethod
    def splitText(text: str, sep: str = ' ', maxLength: int = 90):
        lists = []
        words = text.split(sep)
        currentText = words[0] + sep
        currentLength = len(words[0] + sep)
        for word in words[1:]:
            if currentLength + len(word + sep) < maxLength:
                currentText += (word + sep)
                currentLength += len(word + sep)
            else:
                lists.append(currentText)
                currentText = word + sep
                currentLength = len(word + sep)

        if not currentText == '':
            if currentText.endswith(', '):
                currentText = currentText[:-2]
            lists.append(currentText)
        return lists

    def argStrings(self, required: bool = False, typeHint: bool = True, objectName: str = '') -> str:
        if len(self.args) == 0:
            return ''
        strings = self.argString(0, typeHint, objectName=objectName)
        for index in range(1, len(self.args)):
            if required and not self.args[index].required:
                continue
            strings += ', {}'.format(self.argString(index, typeHint, objectName=objectName))
        return strings

    def argStringsSplitLists(self, sep: str = ', ', maxLength: int = 90, typeHint: bool = True, objectName: str = ''):
        return self.splitText(self.argStrings(typeHint=typeHint, objectName=objectName), sep, maxLength)

    def requiredArgStringsSplitLists(self, sep: str = ', ', maxLength: int = 90, typeHint: bool = True):
        return self.splitText(self.argStrings(True, typeHint), sep, maxLength)

    @staticmethod
    def simplifiedDocs(docs: list[str]):
        simplifiedDocs: list[str] = []
        for doc in docs:
            links = re.findall(r'\[[\w\s]+\]\(.+?\)', doc)
            if len(links) > 0:
                doc = re.sub(r'\[([\w\s]+)\]\(.+?\)', '\g<1>', doc)
            simplifiedDocs.append(doc)
        return simplifiedDocs

    @staticmethod
    def splitStrings(strings: list[str], sep: str = ' ', maxLength: int = 90):
        splitStrings = []
        for string in Method.simplifiedDocs(strings):
            splitStrings += Method.splitText(string, sep, maxLength)
        return splitStrings

    def splitDocs(self, sep: str = ' ', maxLength: int = 90):
        return self.splitStrings(self.docs, sep, maxLength)

    def splitReturnDocs(self, sep: str = ' ', maxLength: int = 90):
        return self.splitStrings(self.returnDocs, sep, maxLength)

    def splitExceptionsDocs(self, sep: str = ' ', maxLength: int = 90):
        return self.splitStrings(self.exceptions, sep, maxLength)

    def splitArgumentDocs(self, index: int, sep: str = ' ', maxLength: int = 90):
        return self.splitStrings(self.simplifiedDocs(self.args[index].docs), sep, maxLength)

