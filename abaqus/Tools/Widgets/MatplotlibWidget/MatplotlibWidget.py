import re

import matplotlib.pyplot as plt
from PyQt5.QtCore import QStandardPaths, Qt, pyqtSignal, QFileInfo
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QAction, QFileDialog, QMessageBox, QTabWidget, QToolBar, QVBoxLayout, QWidget, QTextEdit)
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from .pyqtconsole import highlighter

from .MatplotlibPythonConsole import MatplotlibPythonConsole
from .PythonHighlighter import PythonHighlighter

from .icons_rc import *

# Just try to tell the IDE it is inherited by QToolBar to get the code hint

defaultHeader = """import matplotlib.pyplot as plt
import pandas as pd

fig = self.getFigure()
"""

class Toolbar(NavigationToolbar, QToolBar):
    def __init__(self, canvas, parent, coordinates=True):
        super().__init__(canvas, parent, coordinates)


class MatplotlibWidget(QWidget):
    textChanged = pyqtSignal(object)
    readyToBeActive = pyqtSignal(object)

    @staticmethod
    def defaultHeader() -> str:
        return defaultHeader

    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setParent(self)
        self.toolbar = Toolbar(self.canvas, self)
        self.saveFilepath = QStandardPaths.writableLocation(QStandardPaths.DocumentsLocation)

        # Layout
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(self.toolbar)

        # Code Tab
        self.codeEditor = QTextEdit()
        self.originalCode = self.defaultHeader()
        self.codeEditor.append(self.originalCode)
        self.codeEditor.setReadOnly(False)
        self.pythonHighlighter = PythonHighlighter(self.codeEditor.document())

        # Python Console Tab
        self.pythonConsole = MatplotlibPythonConsole(formats={
            'keyword': highlighter.format('blue', 'bold'),
            'operator': highlighter.format('red'),
            'brace': highlighter.format('darkGray'),
            'defclass': highlighter.format('black', 'bold'),
            'string': highlighter.format('magenta'),
            'string2': highlighter.format('darkMagenta'),
            'comment': highlighter.format('darkGreen', 'italic'),
            'self': highlighter.format('black', 'italic'),
            'numbers': highlighter.format('brown'),
            'inprompt': highlighter.format('darkBlue', 'bold'),
            'outprompt': highlighter.format('darkRed', 'bold'),
        })
        self.pythonConsole.interpreter.figure = self.figure
        self.pythonConsole.interpreter.canvas = self.canvas
        # self.pythonConsole.eval_in_thread()
        self.pythonConsole.eval_queued()

        # Save to Python Action
        self.actionSave = QAction(QIcon(':/icons/save.png'), 'Save')
        self.actionSave.setToolTip('Save to .py file')
        self.actionSave.triggered.connect(self.save)

        # Update Action
        self.actionUpdate = QAction(QIcon(':/icons/update.png'), 'Update')
        self.actionUpdate.setToolTip('Update figure')
        self.actionUpdate.triggered.connect(self.update)

        # Restore Action
        self.actionRestore = QAction(QIcon(':/icons/restore.png'), 'Restore')
        self.actionRestore.setToolTip('Restore figure')
        self.actionRestore.triggered.connect(self.restore)

        # Add Actions to Toolbar
        self.toolbar.addAction(self.actionSave)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.actionUpdate)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.actionRestore)
        self.toolbar.addSeparator()
        self.toolbar.setToolButtonStyle(Qt.ToolButtonIconOnly)

        # Add Tabs to TabWidget
        self.tabWidget = QTabWidget()
        self.tabWidget.setTabPosition(QTabWidget.South)
        self.tabWidget.addTab(self.canvas, 'Figure')
        self.tabWidget.addTab(self.codeEditor, 'Code')
        self.tabWidget.addTab(self.pythonConsole, 'Python Console')

        # Set Layout
        self.layout.addWidget(self.tabWidget)
        self.setLayout(self.layout)

    def getFigure(self):
        return self.figure

    def draw(self):
        self.canvas.draw()

    def update(self):
        self.figure.clear()
        code = self.codeEditor.toPlainText()
        keys, values = ['fig', 'canvas'], ['self.figure', 'self.canvas']
        for key, value in zip(keys, values):
            pattern = '\n{}\s?=\s?.+\n'.format(key)
            code = re.sub(pattern, '\n{} = {}\n'.format(key, value), code)
        self.pythonConsole.runsource(code)
        self.draw()
        self.tabWidget.setCurrentIndex(0)
        
    def restore(self):
        self.codeEditor.setText(self.originalCode)
        self.update()

    def save(self):
        filepath = QFileDialog.getSaveFileName(self, caption='Save to .py File', directory='',
                                               filter='Python File (*.py)')[0].strip()
        if not QFileInfo(filepath).dir().exists():
            raise FileNotFoundError('Directory not exists')
        try:
            file = open(filepath, 'w+')
            code = self.codeEditor.toPlainText().replace('fig = self.getFigure()', 'fig = plt.figure()')
            code += '\nplt.show()'
            file.write(code)
        except Exception as e:
            QMessageBox.warning(self, 'Warning', repr(e))

    def setCode(self, code: str, original: bool = True):
        self.codeEditor.setText(code)
        if original:
            self.originalCode = code
        self.update()

    def codeTextChanged(self):
        self.textChanged.emit(self.codeEditor.toPlainText())
