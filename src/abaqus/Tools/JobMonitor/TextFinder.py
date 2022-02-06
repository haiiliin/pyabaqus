from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QDialog, QApplication, QStyle

from .Ui_TextFinder import Ui_TextFinder


class TextFinder(QDialog):
    readyToFind = pyqtSignal(bool)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_TextFinder()
        self.ui.setupUi(self)
        self.raise_()
        self.setWindowIcon(QApplication.style().standardIcon(QStyle.SP_TitleBarMenuButton))

        self.ui.previousButton.clicked.connect(self.findPrevious)
        self.ui.nextButton.clicked.connect(self.findNext)

    def findPrevious(self):
        self.readyToFind.emit(False)

    def findNext(self):
        self.readyToFind.emit(True)

    def textToFind(self):
        return self.ui.textToFind.text()
