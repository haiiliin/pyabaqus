import os.path
import re

from PyQt5.QtWidgets import (QMainWindow)

from Ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):
    isNew: bool = True
    isSaved: bool = False
    isFileGenerated: bool = False

    currentVersion = 'V1.0'

    def __init__(self, parent=None) -> None:
        super().__init__(parent=parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # self.ui.original.textChanged.connect(self.onTextChanged)
        self.ui.actionSetupSubModule.triggered.connect(self.setupSubModule)
        self.ui.actionSetupSketch.triggered.connect(self.setupSketch)

    def setupSubModule(self):
        texts = self.ui.original.toPlainText().lstrip().rstrip().split()
        if len(texts) < 3:
            return
        filePath, baseType, member = texts[0], texts[1], texts[2]
        modelText = 'import typing\nfrom abaqusConstants import *\nfrom ..Model.ModelBase import ModelBase\n\n'
        modelText += '\n\nclass {}Model(ModelBase, Parents):\n'.format(baseType)
        parents = []
        if os.path.exists(filePath) and os.path.isdir(filePath):
            files = os.listdir(filePath)
            for file in files:
                Type = file[:-3]
                if not file.endswith('.py') or file == '__init__.py':
                    continue

                with open('{}\\{}'.format(filePath, file), 'r+', encoding='utf-8') as f:
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
                    methodDefinition = 'self.{}[{}] = {} = {}({})\n'.format(
                        member, 'name', member[:-2] if member.endswith('es') and not member == 'amplitudes' else
                        member[:-1], Type, ', '.join(args))
                    methodDefinition += 8 * ' ' + 'return {}'.format(
                        member[:-2] if member.endswith('es') and not member == 'amplitudes' else member[:-1])
                    methodString = re.sub('({}\([\s\S]+?\)):'.format(Type), '\g<1> -> {}:'.format(Type), methodString)
                    methodString = methodString.replace('pass', methodDefinition)

                    importString = 'from .{} import {}\n'.format(Type, Type)
                    parents.append(Type)
                    if importString not in modelText:
                        modelText = importString + modelText

                    if 'def {}('.format(Type) not in modelText:
                        modelText = '\n'.join([modelText, methodString])
                        modelText = re.sub('\n\n+', '\n\n', modelText)
        modelText = modelText.replace('class {}Model(ModelBase, Parents):\n'.format(baseType),
                                      'class {}Model(ModelBase):\n'.format(baseType))
        self.ui.replaced.setPlainText(modelText)

    def setupSketch(self):
        texts = self.ui.original.toPlainText().lstrip().rstrip().split()
        if len(texts) < 2:
            return
        filePath, baseType = texts[0], texts[1]
        imports = ''
        if len(texts) > 2:
            imports = ' '.join(texts[2:])
        if not os.path.exists(filePath) or os.path.isdir(filePath):
            return
        with open(filePath, 'r+', encoding='utf-8') as f:
            text = f.read()
            f.close()
        methodStrings = re.findall('\n\s+def \w+\(self,[\s\S]+?pass\n', text)
        for methodString in methodStrings:
            name = re.sub('\n\s+def (\w+)\(self,[\s\S]+?pass\n', '\g<1>', methodString)
            methodString = methodString.replace(name, '__init__')
            text = 'from .{} import {}\n'.format(baseType, baseType)
            text += '{}\n'.format(imports)
            text += '\n\nclass {}({}):\n'.format(name, baseType)
            text += methodString
            with open(os.path.join(os.path.dirname(filePath), '{}.py'.format(name)), 'w+', encoding='utf-8') as f:
                f.write(text)
                f.close()
            self.ui.replaced.appendPlainText(text)

    def onTextChanged(self):
        text = self.ui.original.toPlainText()
        text = re.sub('typing.Union\[.+?\]', 'None', text)
        text = re.sub('\s+?', '', text)
        args = [arg.split(':')[0] for arg in text.split(',')]
        self.ui.replaced.setPlainText(', '.join(args))
