import os

import pandas as pd
from PyQt5.QtWidgets import QWidget

from .Model import Model
from .Ui_ExecutorSubWidget import Ui_ExecutorSubWidget


class ExecutorSubWidget(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_ExecutorSubWidget()
        self.ui.setupUi(self)

        self.model = Model()

    def saveView2Model(self):
        self.model.workDirectory = self.ui.cwd.toPlainText()
        self.model.modelScript = self.ui.modelScript.text()
        self.model.input = self.ui.input.text()
        self.model.user = self.ui.user.text()
        self.model.odb = self.ui.odb.text()
        self.model.outputScript = self.ui.outputScript.text()
        self.model.data = self.ui.data.text()
        self.model.x = self.ui.x.currentText()
        self.model.ys = self.ui.ys.text().split(',')
        self.model.xlabel = self.ui.xlabel.text()
        self.model.ylabel = self.ui.ylabel.text()
        self.model.title = self.ui.title.text()

    def loadModel2View(self):
        self.ui.cwd.setPlainText(self.model.workDirectory)
        self.ui.modelScript.setText(self.model.modelScript)
        self.ui.input.setText(self.model.input)
        self.ui.user.setText(self.model.user)
        self.ui.odb.setText(self.model.odb)
        self.ui.outputScript.setText(self.model.outputScript)
        self.ui.input.setText(self.model.input)
        self.ui.data.setText(self.model.data)
        self.ui.ys.setText(','.join(self.model.ys))
        self.ui.xlabel.setText(self.model.xlabel)
        self.ui.ylabel.setText(self.model.ylabel)
        self.ui.title.setText(self.model.title)

        dataFilePath = os.path.join(self.model.absWorkDirectory(), self.model.data)
        if os.path.exists(dataFilePath) and os.path.isfile(dataFilePath):
            df = pd.read_csv(dataFilePath)
            self.ui.x.clear()
            self.ui.x.addItems(df.columns)
            self.ui.y.clear()
            self.ui.y.addItems(df.columns)
            if self.model.x in df.columns:
                self.ui.x.setCurrentText(self.model.x)
