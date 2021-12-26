import os
import time

from ObjectParser.ObjectParser import ObjectParser

# parser = ObjectParser(filePath='AbaqusScriptingReferenceGuide-Markdown-2022\\Python\\Part\\Part.md')
# parser.parse().toAbaqusObject(searchParentDir='abaqus').toPythonScript(fileDir='abaqus\\Part', searchDir='abaqus')
#
#
# parser = ObjectParser(filePath='AbaqusScriptingReferenceGuide-Markdown-2022\\Python\\BoundaryCondition\\AccelerationBC.md')
# parser.parse().toAbaqusObject(searchParentDir='AbaqusScriptingReferenceGuide-Markdown-2022\\Python').toPythonScript(fileDir='abaqus\\BoundaryCondition', searchDir='abaqus')

start_time = time.time()

if not os.path.exists(os.path.join('abaqus', '__init__.py')):
    with open(os.path.join('abaqus', '__init__.py'), 'w+') as file:
        file.write('')
        file.close()

fileDir = 'AbaqusScriptingReferenceGuide-Markdown-2022\\Python'
modules = os.listdir(fileDir)
for module in modules:
    if not os.path.isdir(os.path.join(fileDir, module)):
        continue

    moduleMDDir = os.path.join(fileDir, module)
    moduleAbqDir = 'abaqus\\{}'.format(module)

    if not os.path.exists(moduleAbqDir):
        os.makedirs(moduleAbqDir)

    if not os.path.exists(os.path.join(moduleAbqDir, '__init__.py')):
        with open(os.path.join(moduleAbqDir, '__init__.py'), 'w+') as file:
            file.write('')
            file.close()

    with open(os.path.join(moduleAbqDir, '__init__.py'), 'r+', encoding='utf-8') as f:
        text = f.read().lstrip().rstrip()
    files = os.listdir(moduleAbqDir)
    importString = ''
    for file in files:
        if not file.endswith('.md'):
            continue
        with open(os.path.join(moduleAbqDir, file), 'r+', encoding='utf-8') as f1:
            text1 = f1.read()
        objectName = file.split('.')[0]
        if 'class {}'.format(objectName) in text1:
            importString += 'from .{} import {}\n'.format(objectName, objectName)
    importString = importString.rstrip() + '\n'
    with open(os.path.join(moduleAbqDir, '__init__.py'), 'w+', encoding='utf-8') as f:
        f.write(importString)
        f.close()

    files = os.listdir(moduleMDDir)
    for file in files:
        if file == 'README.md' or not file.endswith('md'):
            continue
        filePath = os.path.join(moduleMDDir, file)
        parser = ObjectParser(filePath=filePath)
        parser.parse().toAbaqusObject(
            searchParentDir='AbaqusScriptingReferenceGuide-Markdown-2022\\Python'
        ).toPythonScript(
            fileDir=moduleAbqDir, searchDir='abaqus'
        )

    print('\n  # Finished processing {} module, took {:.2f} seconds'.format(module, time.time() - start_time))
