import os
import re


with open('abaqus\\Material\\BaseMaterial.py', 'r+') as f:
    baseMaterialText = f.read()
    f.close()

materialText = 'import typing\n'
materialText += 'from abaqusConstants import *\n'
materialText += 'from .BaseMaterial import BaseMaterial\n\n\n'
materialText += 'class Material(BaseMaterial):\n\n'
files = os.listdir('abaqus\\Interaction')
for file in files:
    if not file.endswith('.py') or file in ['Material.py', 'BaseMaterial.py', '__init__.py']:
        continue

    filePath = 'abaqus\\Material\\{}'.format(file)
    Type = file[:-3]

    if len(re.findall('{}:[\s\S]+?:[\s\S]+?=[\s\S]+?\n'.format(Type[0].lower() + Type[1:]), baseMaterialText)) == 0:
        continue

    with open(filePath, 'r+', encoding='utf-8') as f:
        text = f.read()
        f.close()

    foundMethods: list[str] = re.findall('\n\s+def __init__[\s\S]+?pass\n', text)  # (\s+@typing.overload)?
    if len(foundMethods) > 0:
        methodString = foundMethods[0].replace('def __init__', 'def {}'.format(Type))
        methodString = methodString.replace('\n        super().__init__()', '')
        argStrings = re.findall('\(self,[\s\S]+?\):', methodString)
        if len(argStrings) == 0:
            continue

        argStrings[0] = re.sub('typing.Union\[.+?\]', 'None', argStrings[0])
        argStrings[0] = re.sub('\s+?', '', argStrings[0])
        args = [arg.split(':')[0] for arg in argStrings[0][6:][:-2].split(',')]
        methodDefinition = 'self.{} = {}({})\n'.format(Type[0].lower() + Type[1:], Type, ', '.join(args))
        methodDefinition += 8 * ' ' + 'return self.{} '.format(Type[0].lower() + Type[1:])
        methodString = re.sub('({}\([\s\S]+?\)):'.format(Type), '\g<1> -> {}:'.format(Type), methodString)
        methodString = methodString.replace('pass', methodDefinition)

        importString = 'from .{} import {}\n'.format(Type, Type)
        if importString not in materialText:
            materialText = importString + materialText

        if 'def {}'.format(Type) not in materialText:
            materialText = '\n'.join([materialText, methodString])
            materialText = re.sub('\n\n+', '\n\n', materialText)

with open('abaqus\\Material\\Material.py', 'w+', encoding='utf-8') as f:
    f.write(materialText)
    f.close()
