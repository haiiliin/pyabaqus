import os
import re


class Guess:

    @staticmethod
    def removeMarkdownLinks(text: str):
        links = re.findall(r'\[.+?\]\(.+?\)', text)
        simplifiedText = text
        if len(links) > 0:
            simplifiedText = re.sub(r'\[([\w\s]+)\]\(.+?\)', '\g<1>', text)
        return simplifiedText

    @staticmethod
    def parserMarkdownLink(text: str):
        links = re.findall(r'\[.+?\]\(.+?\)', text)
        if len(links) > 0:
            label = re.sub(r'\[(.+?)\]\(.+?\)', '\g<1>', links[0])
            link = re.sub(r'\[.+?\]\((.+?)\)', '\g<1>', links[0])
            return label, link
        else:
            raise ValueError('Parser with error')

    @staticmethod
    def guessParent(text: str):
        parent = ''
        lists = re.findall(r'is derived from the \w+ object', Guess.removeMarkdownLinks(text))
        if len(lists) > 0:
            parent = re.sub(r'is derived from the (\w+) object', '\g<1>', lists[0])
        return parent

    @staticmethod
    def findParentFilePath(userDefinedType: str, searchDir: str):
        if not os.path.isdir(searchDir):
            return ''

        files = os.listdir(searchDir)
        for file in files:

            if os.path.isdir(os.path.join(searchDir, file)):
                foundDir = Guess.findParentFilePath(userDefinedType, os.path.join(searchDir, file))
                if not foundDir == '':
                    return foundDir
            elif os.path.isfile(os.path.join(searchDir, file)) and file.endswith('.md'):
                filePath = os.path.join(searchDir, file)
                with open(filePath, 'r+', encoding='utf-8') as f:
                    text = f.read()
                    if text.startswith('# {} object'.format(userDefinedType)):
                        return filePath
                    f.close()
        return ''

    @staticmethod
    def guessType(text: str):
        text = Guess.removeMarkdownLinks(text)
        argType, default = 'str', None

        lists = re.findall(r'The default.*? is \w+?\.', text)
        if len(lists) > 0 and not lists[0] == 'The default value is an empty string.':
            default = lists[0].split()[-1][:-1]
            if default == 'zero':
                default = '0.0'

        defaults = {
            'int': 'None', 'float': 'None', 'Boolean': 'OFF', 'str': "''", 'tuple': '()', 'SymbolicConstant': 'None',
            'Repository': 'None', 'dict': '{}'
        }

        userDefinedType = None

        if text.startswith('A String'):
            argType = 'str'
        elif text.startswith('A Boolean') or text.startswith('A boolean'):
            argType = 'Boolean'
        elif text.startswith('A Dictionary') or text.startswith('A dictionary'):
            argType = 'dict'
        elif 'A pair of Floats' in text and 'sequence' not in text:
            argType = 'tuple[float]'
        elif 'SymbolicConstant' in text and 'Float' in text:
            argType = 'typing.Union[SymbolicConstant,float]'
        elif 'Float' in text and 'sequence' not in text:
            argType = 'float'
        elif 'SymbolicConstant' in text:
            argType = 'SymbolicConstant'
        elif 'Int' in text and 'sequence' not in text:
            argType = 'int'
        elif 'tuple' in text or 'Tuple' in text:
            argType = 'tuple'
        elif 'A sequence' in text:
            argType = 'tuple'
            lists = re.findall(r'A sequence of \w+? objects', text)
            if len(lists) > 0:
                userDefinedType = lists[0].split()[-2]
                argType = 'tuple[{}]'.format(userDefinedType)
        elif len(re.findall(r'An? \w+? object', text)) > 0:
            lists = re.findall(r'An? \w+? object', text)
            userDefinedType = lists[0].split()[1]
            argType = userDefinedType
        elif len(re.findall(r'A repository of \w+? objects', text)) > 0:
            lists = re.findall(r'A repository of \w+? objects', text)
            userDefinedType = lists[0].split()[-2] + ' ' + 'Repository'
            argType = 'Repository[str, {}]'.format(lists[0].split()[-2])

        argType.capitalize()

        if default is None:
            if argType in defaults.keys():
                default = defaults[argType]
            elif argType.startswith('tuple'):
                default = '()'
            else:
                default = 'None'

        return argType, default, userDefinedType
