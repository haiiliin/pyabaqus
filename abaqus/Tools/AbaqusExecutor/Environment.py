import os

from PyQt5.QtWidgets import QDialog, QFileDialog

from .Ui_Environment import Ui_Environment


class Environment(QDialog):

    def __init__(self, parent=None, abaqus: str = ''):
        super().__init__(parent)
        self.ui = Ui_Environment()
        self.ui.setupUi(self)
        self.ui.abaqusCommand.setText(abaqus)
        self.ui.browse.clicked.connect(self.browse)

        self.abaqus = abaqus

    def browse(self):
        filePath = QFileDialog.getOpenFileName(self, caption='Select output script', directory=os.path.dirname(self.abaqus),
                                               filter='Abaqus command (*.bat)')
        if not os.path.exists(filePath[0]):
            return
        self.abaqus = filePath[0]
        self.ui.abaqusCommand.setText(filePath[0])

    def abaqusCommand(self):
        return self.abaqus
