import os
import re


modelFilePath = 'abaqus\\Model\\Model.py'
with open(modelFilePath, 'r+', encoding='utf-8') as f:
    modelText = f.read()
    f.close()

importString = re.findall('^[\s\S]+?class PolarityAssignments:\s+pass\n', modelText)
importString = importString[0]

modules = {
    'Amplitude': 'Amplitude',
    'BoundaryCondition': 'BoundaryCondition',
    'Constraint': 'Constraint',
    'Interaction': 'Interaction',
    'LoadAndLoadCase': 'Load',
    'Step': 'AnalysisStep',
    'Section': 'Section',
    'Sketcher': 'ConstrainedSketch',
    'PredefinedField': 'PredefinedField',
    # 'Part': 'Part',
    # 'Material': 'Material'
}

members = {
    'Amplitude': 'amplitudes',
    'BoundaryCondition': 'boundaryConditions',
    'Constraint': 'constraints',
    'Interaction': 'interactions',
    'LoadAndLoadCase': 'loads',
    'Step': 'steps',
    'Section': 'sections',
    'Sketcher': 'sketches',
    'PredefinedField': 'predefinedFields'
    # 'Part': 'parts',
    # 'Material': 'materials'
}

methods = {}
modelText = importString
modelText += '\n\nclass Model(BaseModel):\n'
for module, baseType in modules.items():

    moduleDir = 'abaqus\\{}'.format(module)
    if not os.path.isdir(moduleDir):
        continue
    files = os.listdir(moduleDir)
    moduleTypes = []
    for file in files:
        if not file.endswith('.py') or file == '__init__.py':
            continue

        Type = file[:-3]
        if Type == 'Pressure':
            a = 1
        filePath = 'abaqus\\{}\\{}'.format(module, file)
        with open(filePath, 'r+', encoding='utf-8') as f:
            text = f.read()
            f.close()
        actualBaseTypes = re.findall('class \w+\(\w+\):', text)
        actualBaseType = ''
        if len(actualBaseTypes) > 0:
            actualBaseType = actualBaseTypes[0][len(Type) + 7:][:-2]
        if ('class {}({})'.format(Type, baseType) not in text and
                ('class {}({})'.format(Type, actualBaseType) not in text and baseType in actualBaseType) and
                'class {}'.format(baseType) not in text):
            continue

        moduleTypes.append(Type)

        foundMethods: list[str] = re.findall('\n\s+def __init__[\s\S]+?pass\n', text)  # (\s+@typing.overload)?
        if len(foundMethods) > 0:
            methodString = foundMethods[0].replace('def __init__', 'def {}'.format(Type))
            methodString = methodString.replace('\n        super().__init__()', '')
            argStrings = re.findall('\(self,[\s\S]+?\):', methodString)
            if len(argStrings) == 0 or 'name' not in '\n'.join(argStrings):
                continue

            argStrings[0] = re.sub('typing.Union\[.+?\]', 'None', argStrings[0])
            argStrings[0] = re.sub('\s+?', '', argStrings[0])
            args = [arg.split(':')[0] for arg in argStrings[0][6:][:-2].split(',')]
            methodDefinition = 'self.{}[{}] = {} = {}({})\n'.format(members[module], 'name', members[module][:-2] if members[module].endswith('es') else members[module][:-1], Type, ', '.join(args))
            methodDefinition += 8 * ' ' + 'return {}'.format(members[module][:-2] if members[module].endswith('es') else members[module][:-1])
            methodString = re.sub('({}\([\s\S]+?\)):'.format(Type), '\g<1> -> {}:'.format(Type), methodString)
            methodString = methodString.replace('pass', methodDefinition)

            importString = 'from ..{}.{} import {}\n'.format(module, Type, Type)
            if importString not in modelText:
                modelText = importString + modelText

            if 'def {}('.format(Type) not in modelText:
                modelText = '\n'.join([modelText, methodString])
                modelText = re.sub('\n\n+', '\n\n', modelText)

    methods.update({
        module: moduleTypes
    })

with open(modelFilePath, 'w+', encoding='utf-8') as f:
    f.write(modelText)
    f.close()
