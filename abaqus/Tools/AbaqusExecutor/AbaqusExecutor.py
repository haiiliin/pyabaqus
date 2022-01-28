import os

import pandas as pd
from PyQt5.QtWidgets import QMessageBox

from .AbaqusExecutorView import AbaqusExecutorView


class AbaqusExecutor(AbaqusExecutorView):

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

    def createModel(self):
        activeWindow = self.currentSubWidget()
        if activeWindow is None:
            return

        def setInput():
            files = os.listdir(activeWindow.model.workDirectory)
            for file in files:
                if file.endswith('.inp'):
                    activeWindow.ui.input.setText(file)
                    activeWindow.model.input = file
                    break

        self.process.setWorkingDirectory(os.path.abspath(activeWindow.model.workDirectory))
        self.process.start(*activeWindow.model.createModelCommand())
        self.process.finished.connect(setInput)

    def submit(self):
        activeWindow = self.currentSubWidget()
        if activeWindow is None:
            return

        def setOdb():
            files = os.listdir(activeWindow.model.workDirectory)
            for file in files:
                if file.endswith('.odb'):
                    activeWindow.ui.odb.setText(file)
                    activeWindow.model.odb = file
                    break

        self.thread.setWorkDirectory(os.path.abspath(activeWindow.model.workDirectory))
        self.thread.setJobName(activeWindow.model.jobName())
        self.thread.start()

        self.process.setWorkingDirectory(os.path.abspath(activeWindow.model.workDirectory))
        self.process.start(*activeWindow.model.abaqusCommand())
        self.process.finished.connect(setOdb)

    def extractOutput(self):
        activeWindow = self.currentSubWidget()
        if activeWindow is None:
            return
        self.process.setWorkingDirectory(os.path.abspath(activeWindow.model.workDirectory))
        self.process.start(*activeWindow.model.extractOutputCommand())

    def drawFigures(self):
        activeWindow = self.currentSubWidget()
        if activeWindow is None:
            return

        if not os.path.exists(os.path.join(activeWindow.model.absWorkDirectory(), activeWindow.model.data)):
            QMessageBox.warning(self, 'Warning', 'Please choose data file first')
            return

        x = activeWindow.ui.x.currentText()
        ys = activeWindow.ui.ys.text().split(',')
        xlabel = activeWindow.ui.xlabel.text()
        ylabel = activeWindow.ui.ylabel.text()
        title = activeWindow.ui.title.text()

        fig = activeWindow.ui.fig.getFigure()
        fig.clf()
        ax = fig.add_subplot(111)
        df = pd.read_csv(os.path.join(activeWindow.model.absWorkDirectory(), activeWindow.model.data))
        lines = 0
        for y in ys:
            if y not in df.columns:
                continue
            lines += 1
            ax.plot(df[x], df[y], label=y)
        if lines > 0:
            ax.legend()
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.set_title(title)
        fig.tight_layout()
        activeWindow.ui.fig.draw()

        activeWindow.ui.tabWidget.setCurrentIndex(3)
