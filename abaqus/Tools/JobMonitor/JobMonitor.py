import os.path

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextCursor, QPalette, QKeyEvent, QTextDocument
from PyQt5.QtWidgets import QMainWindow, QPlainTextEdit, QApplication, QStyle, QMessageBox

from .FileMonitorThread import FileMonitorThread
from .TextFinder import TextFinder
from .Ui_JobMonitor import Ui_JobMonitor


class JobMonitor(QMainWindow):

    def __init__(self, parent=None, workDirectory='', jobName='') -> None:
        super().__init__(parent=parent)
        self.ui = Ui_JobMonitor()
        self.ui.setupUi(self)

        self.setWindowIcon(QApplication.style().standardIcon(QStyle.SP_TitleBarMenuButton))

        self.textFinder = None

        self.workDirectory = workDirectory
        self.jobName = jobName
        self.fileMonitorThread = FileMonitorThread()
        self.fileMonitorThread.readyReadStatusFile.connect(self.setStatusFileText)
        self.fileMonitorThread.readyReadMessageFile.connect(self.setMessageFileText)

    def keyPressEvent(self, event: QKeyEvent) -> None:
        if event.modifiers() and Qt.ControlModifier:
            if event.key() == Qt.Key_F:
                self.findText()

    def findText(self):
        if self.textFinder is None:
            self.textFinder = TextFinder(self)
        else:
            self.textFinder.activateWindow()
        index = self.ui.tabWidget.currentIndex()
        currentTextEdit = self.ui.statusFileText if index == 0 else self.ui.messageFileText if index == 1 else None
        if not currentTextEdit.textCursor().selectedText().lstrip().rstrip() == '':
            self.textFinder.ui.textToFind.setText(currentTextEdit.textCursor().selectedText().lstrip().rstrip())
        self.textFinder.show()
        self.textFinder.readyToFind.connect(self.showFoundText)

    def showFoundText(self, findNext: bool):
        textToFind = self.textFinder.textToFind()
        index = self.ui.tabWidget.currentIndex()
        currentTextEdit = self.ui.statusFileText if index == 0 else self.ui.messageFileText if index == 1 else None
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
        self.setText(text, self.ui.statusFileText)

    def setMessageFileText(self, text: str):
        self.setText(text, self.ui.messageFileText)

    def setWorkDirectory(self, workDirectory: str):
        self.workDirectory = workDirectory
        self.fileMonitorThread.setWorkDirectory(workDirectory)

    def setJobName(self, jobName: str):
        self.jobName = jobName
        self.fileMonitorThread.setJobName(jobName)
        self.ui.jobName.setText(os.path.join(self.workDirectory, jobName))

    def run(self):
        self.fileMonitorThread.start()
