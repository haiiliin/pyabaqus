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

        self.ui.original.textChanged.connect(self.onTextChanged)

    def onTextChanged(self):
        text = self.ui.original.toPlainText()
        text = re.sub('typing.Union\[.+?\]', 'None', text)
        text = re.sub('\s+?', '', text)
        args = [arg.split(':')[0] for arg in text.split(',')]
        self.ui.replaced.setPlainText(', '.join(args))
