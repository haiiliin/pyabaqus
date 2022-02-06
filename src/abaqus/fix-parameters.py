import os
import re


def FixParametersInDocString(path: str):
    print('Processing {} package'.format(path))
    files = os.listdir(path)
    for file in files:
        filePath = '{}\\{}'.format(path, file)
        if file.startswith('__') or file.startswith('.'):
            continue
        elif os.path.isdir(filePath):
            FixParametersInDocString(filePath)
        elif os.path.isfile(filePath) and file.endswith('.py'):
            with open(filePath, 'r+', encoding='utf-8') as f:
                text = f.read()
                f.close()
            items = re.findall('        """\w+[\w\W]+?\n        \w+\n        \s+\w', text)
            for item in items:
                if 'Parameters' in item:
                    continue
                newItem = re.sub('(        """\w+[\w\W]+?\n        )(\w+\n        \s+\w)',
                                 '\g<1>\n        Parameters\n        ----------\n        \g<2>', item)
                text = text.replace(item, newItem)
            text = re.sub('(Parameters\s+----------\n)+', '\g<1>', text)
            with open(filePath, 'w+', encoding='utf-8') as f:
                f.write(text)
                f.close()

FixParametersInDocString('abaqus')
