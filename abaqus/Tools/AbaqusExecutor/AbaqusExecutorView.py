import os
import typing

import pandas as pd
from PyQt5.QtCore import Qt, QProcess
from PyQt5.QtGui import QKeyEvent, QPalette, QTextDocument, QTextCursor
from PyQt5.QtWidgets import QMainWindow, QApplication, QStyle, QFileDialog, QMessageBox, QPlainTextEdit, QMdiSubWindow, \
    QDialog

from .Environment import Environment
from .ExecutorSubWidget import ExecutorSubWidget
from .Setting import Setting
from .Ui_AbaqusExecutor import Ui_AbaqusExecutor
from ..FileMonitorThread import FileMonitorThread
from ..Widgets.TextFinder import TextFinder


class AbaqusExecutorView(QMainWindow):

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.ui = Ui_AbaqusExecutor()
        self.ui.setupUi(self)
        self.setWindowIcon(QApplication.style().standardIcon(QStyle.SP_TitleBarMenuButton))
        self.connectSignals()

        self.textFinder = None
        self.subWindows: list[ExecutorSubWidget] = []

        self.setting = Setting()

        self.thread = FileMonitorThread()
        self.thread.readyReadStatusFile.connect(self.setStatusFileText)
        self.thread.readyReadMessageFile.connect(self.setMessageFileText)

        self.process = QProcess()
        self.process.setReadChannel(QProcess.StandardOutput)
        self.process.finished.connect(self.thread.terminate)
        self.process.readyReadStandardOutput.connect(self.readStandardOutput)

    def new(self, clicked: bool = False, filePath: str = None):
        widget = ExecutorSubWidget(self.ui.mdiArea)
        widget.ui.cwd.setPlainText(os.path.abspath(widget.model.workDirectory))
        widget.ui.browseCwd.clicked.connect(self.browseCwd)
        widget.ui.browseModelScript.clicked.connect(self.browseModelScript)
        widget.ui.browseInput.clicked.connect(self.browseInputFile)
        widget.ui.browseUser.clicked.connect(self.browseUserSubroutine)
        widget.ui.browseOdb.clicked.connect(self.browseOdb)
        widget.ui.browseOutputScript.clicked.connect(self.browseOutputScript)
        widget.ui.browseData.clicked.connect(self.browseDataFile)
        widget.ui.runModel.clicked.connect(self.createModel)
        widget.ui.submit.clicked.connect(self.submit)
        widget.ui.runOutput.clicked.connect(self.extractOutput)
        widget.ui.drawFigures.clicked.connect(self.drawFigures)
        widget.ui.addY.clicked.connect(self.addYAxis)
        widget.model.setAbaqusCommand(self.setting['abaqus'])

        subWindow = QMdiSubWindow()
        subWindow.setWindowFlags(Qt.WindowSystemMenuHint | Qt.WindowTitleHint | Qt.WindowMinMaxButtonsHint)
        subWindow.setWidget(widget)
        self.ui.mdiArea.addSubWindow(subWindow)

        if filePath is not None:
            widget.model.load(filePath)
            widget.loadModel2View()
            subWindow.setWindowTitle(filePath)
        else:
            filePath = QFileDialog.getSaveFileName(self, caption='Select Abaqus Executor file',
                                                   directory=widget.model.workDirectory,
                                                   filter='Abaqus executor file (*.abqjson)')
            if not os.path.exists(os.path.dirname(filePath[0])):
                return
            widget.model.workDirectory = os.path.dirname(filePath[0])
            widget.model.fileName = os.path.basename(filePath[0])
            widget.model.save(filePath[0])
            widget.loadModel2View()
            subWindow.setWindowTitle(filePath[0])

        widget.show()

    def open(self):
        filePath = QFileDialog.getOpenFileName(self, caption='Select Abaqus Executor file', directory='',
                                               filter='Abaqus executor file (*.abqjson)')
        if not os.path.exists(filePath[0]):
            return
        self.new(filePath=filePath[0])

    def save(self):
        activeWindow = self.currentSubWidget()
        activeWindow.saveView2Model()
        activeWindow.model.save()
        self.statusBar().showMessage('File {} saved successfully'.format(activeWindow.model.absFilePath()), 4000)

    def saveAs(self):
        activeWindow = self.currentSubWidget()
        activeWindow.saveView2Model()
        filePath = QFileDialog.getSaveFileName(self, caption='Select Abaqus input file',
                                               directory=activeWindow.model.workDirectory,
                                               filter='Abaqus executor file (*.abqjson)')
        if not os.path.exists(os.path.dirname(filePath[0])):
            return
        activeWindow.model.save(filePath[0])
        self.statusBar().showMessage('File {} saved successfully'.format(filePath[0]), 4000)

    def abaqus(self):
        pass

    def abaqusCAE(self):
        pass

    def environment(self):
        env = Environment(self, abaqus=self.setting['abaqus'])
        ret = env.exec()
        if ret == QDialog.Accepted:
            self.setting['abaqus'] = env.abaqusCommand()

        for subWindows in self.ui.mdiArea.subWindowList():
            widget: ExecutorSubWidget = subWindows.widget()
            widget.model.setAbaqusCommand(self.setting['abaqus'])

    def createModel(self):
        pass

    def submit(self):
        pass

    def extractOutput(self):
        pass

    def drawFigures(self):
        pass

    def addYAxis(self):
        activeWindow = self.currentSubWidget()
        y = activeWindow.ui.y.currentText()
        o = activeWindow.ui.ys.text()
        ys = o.split(',') if not o.lstrip().rstrip() == '' else []
        if y not in ys:
            ys += [y]
        activeWindow.ui.ys.setText(','.join(ys))

    def currentSubWidget(self) -> typing.Optional[ExecutorSubWidget]:
        if self.ui.mdiArea.currentSubWindow() is None:
            QMessageBox.warning(self, 'Warning', 'Please open or create a project first')
            return
        return self.ui.mdiArea.currentSubWindow().widget()

    def currentSubWindow(self) -> typing.Optional[ExecutorSubWidget]:
        if self.ui.mdiArea.currentSubWindow() is None:
            QMessageBox.warning(self, 'Warning', 'Please open or create a project first')
            return
        return self.ui.mdiArea.currentSubWindow()

    def keyPressEvent(self, event: QKeyEvent) -> None:
        if event.modifiers() and Qt.ControlModifier:
            if event.key() == Qt.Key_F:
                self.findText()

    def findText(self):
        if self.textFinder is None:
            self.textFinder = TextFinder(self)
        else:
            self.textFinder.activateWindow()
        index = self.currentSubWidget().ui.tabWidget.currentIndex()
        currentTextEdit = self.currentSubWidget().ui.sta if index == 1 else self.currentSubWidget().ui.msg if index == 2 else None
        if currentTextEdit is None:
            return
        if not currentTextEdit.textCursor().selectedText().lstrip().rstrip() == '':
            self.textFinder.ui.textToFind.setText(currentTextEdit.textCursor().selectedText().lstrip().rstrip())
        self.textFinder.show()
        self.textFinder.readyToFind.connect(self.showFoundText)

    def showFoundText(self, findNext: bool):
        textToFind = self.textFinder.textToFind()
        index = self.currentSubWidget().ui.tabWidget.currentIndex()
        currentTextEdit = self.currentSubWidget().ui.sta if index == 1 else self.currentSubWidget().ui.msg if index == 2 else None
        if currentTextEdit is None:
            return
        if currentTextEdit is not None:
            if (not findNext and (currentTextEdit.find(textToFind, QTextDocument.FindBackward)) or
                    (findNext and currentTextEdit.find(textToFind))):
                palette = currentTextEdit.palette()
                palette.setColor(QPalette.Highlight, palette.color(QPalette.Active, QPalette.Highlight))
                currentTextEdit.setPalette(palette)
            else:
                btn = QMessageBox.question(self, 'Find', 'Find nothing, move to the {}?'.format('beginning' if findNext else 'end'),
                                           QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.NoButton)
                if btn == QMessageBox.Yes:
                    textCursor = currentTextEdit.textCursor()
                    textCursor.movePosition(QTextCursor.Start if findNext else QTextCursor.End)
                    currentTextEdit.setTextCursor(textCursor)
                    self.textFinder.activateWindow()

    @staticmethod
    def setText(text: str, objectToSetText: QPlainTextEdit):
        oldText = objectToSetText.toPlainText()
        if not len(oldText.splitlines()) == len(text.splitlines()):
            objectToSetText.setPlainText(text)
            textCursor = objectToSetText.textCursor()
            textCursor.movePosition(QTextCursor.End)
            objectToSetText.setTextCursor(textCursor)

    def setStatusFileText(self, text: str):
        self.setText(text, self.currentSubWidget().ui.sta)

    def setMessageFileText(self, text: str):
        self.setText(text, self.currentSubWidget().ui.msg)

    def readStandardOutput(self):
        output = self.process.readAllStandardOutput()
        self.currentSubWidget().ui.cmd.appendPlainText(str(output, encoding='gb18030', errors='ignore'))

    def showTemporaryFiles(self, files: dict[str, str]):
        if 'sta' in files.keys():
            self.currentSubWidget().ui.sta.setPlainText(files['sta'])
        if 'msg' in files.keys():
            self.currentSubWidget().ui.msg.setPlainText(files['msg'])

    def browseCwd(self):
        activeWindow = self.currentSubWidget()
        filePath = QFileDialog.getExistingDirectory(self, caption='Select folder', directory=activeWindow.model.workDirectory)
        self.currentSubWidget().ui.cwd.setPlainText(filePath)
        activeWindow.model['workDirectory'] = filePath
        self.currentSubWindow().setWindowTitle(filePath)

    def browseModelScript(self):
        activeWindow = self.currentSubWidget()
        filePath = QFileDialog.getOpenFileName(self, caption='Select model script', directory=activeWindow.model.workDirectory,
                                               filter='Python script (*.py)')
        if not os.path.exists(filePath[0]):
            return
        self.currentSubWidget().ui.modelScript.setText(os.path.relpath(filePath[0], activeWindow.model.workDirectory))
        activeWindow.model['modelScript'] = os.path.relpath(filePath[0], activeWindow.model.workDirectory)

    def browseJobFile(self):
        activeWindow = self.currentSubWidget()
        filePath = QFileDialog.getOpenFileName(self, caption='Select Abaqus input file', directory=activeWindow.model.workDirectory,
                                               filter='Abaqus input file (*.inp)')
        if not os.path.exists(filePath[0]):
            return
        self.currentSubWidget().ui.job.setText(os.path.relpath(filePath[0], activeWindow.model.workDirectory))
        activeWindow.model['job'] = os.path.relpath(filePath[0], activeWindow.model.workDirectory)

    def browseInputFile(self):
        activeWindow = self.currentSubWidget()
        filePath = QFileDialog.getOpenFileName(self, caption='Select Abaqus input file', directory=activeWindow.model.workDirectory,
                                               filter='Abaqus input file (*.inp)')
        if not os.path.exists(filePath[0]):
            return
        self.currentSubWidget().ui.input.setText(os.path.relpath(filePath[0], activeWindow.model.workDirectory))
        activeWindow.model['input'] = os.path.relpath(filePath[0], activeWindow.model.workDirectory)

    def browseUserSubroutine(self):
        activeWindow = self.currentSubWidget()
        filePath = QFileDialog.getOpenFileName(self, caption='Select Abaqus user subroutine', directory=activeWindow.model.workDirectory,
                                               filter='Abaqus subroutine file (*.for *.f *.c *.cpp *.cxx)')
        if not os.path.exists(filePath[0]):
            return
        self.currentSubWidget().ui.user.setText(os.path.relpath(filePath[0], activeWindow.model.workDirectory))
        activeWindow.model['user'] = os.path.relpath(filePath[0], activeWindow.model.workDirectory)

    def browseOdb(self):
        activeWindow = self.currentSubWidget()
        filePath = QFileDialog.getOpenFileName(self, caption='Select output script',
                                               directory=activeWindow.model.workDirectory,
                                               filter='Abaqus odb file (*.odb)')
        if not os.path.exists(filePath[0]):
            return
        self.currentSubWidget().ui.odb.setText(os.path.relpath(filePath[0], activeWindow.model.workDirectory))
        activeWindow.model['odb'] = os.path.relpath(filePath[0], activeWindow.model.workDirectory)

    def browseOutputScript(self):
        activeWindow = self.currentSubWidget()
        filePath = QFileDialog.getOpenFileName(self, caption='Select output script', directory=activeWindow.model.workDirectory,
                                               filter='Python script (*.py)')
        if not os.path.exists(filePath[0]):
            return
        self.currentSubWidget().ui.outputScript.setText(os.path.relpath(filePath[0], activeWindow.model.workDirectory))
        activeWindow.model['outputScript'] = os.path.relpath(filePath[0], activeWindow.model.workDirectory)

    def browseDataFile(self):
        activeWindow = self.currentSubWidget()
        filePath = QFileDialog.getOpenFileName(self, caption='Select data file', directory=activeWindow.model.workDirectory,
                                               filter='Comma-separated file (*.csv)')
        if not os.path.exists(filePath[0]):
            return
        self.currentSubWidget().ui.data.setText(os.path.relpath(filePath[0], activeWindow.model.workDirectory))
        activeWindow.model['data'] = os.path.relpath(filePath[0], activeWindow.model.workDirectory)
        df = pd.read_csv(filePath[0])
        activeWindow.ui.x.clear()
        activeWindow.ui.x.addItems(df.columns)
        activeWindow.ui.y.clear()
        activeWindow.ui.y.addItems(df.columns)

    def connectSignals(self):
        self.ui.actionNew.triggered.connect(self.new)
        self.ui.actionOpen.triggered.connect(self.open)
        self.ui.actionSave.triggered.connect(self.save)
        self.ui.actionSaveAs.triggered.connect(self.saveAs)

        self.ui.actionModel.triggered.connect(self.createModel)
        self.ui.actionSubmit.triggered.connect(self.submit)
        self.ui.actionOutput.triggered.connect(self.extractOutput)
        self.ui.actionDraw.triggered.connect(self.drawFigures)

        self.ui.actionEnvironment.triggered.connect(self.environment)
