import os

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
        try:
            self.process.setWorkingDirectory(os.path.abspath(activeWindow.model.workDirectory))
            self.process.start(*activeWindow.model.createModelCommand())
            self.process.finished.connect(setInput)
        except Exception as e:
            QMessageBox.warning(self, 'Warning', repr(e))

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
                
        try:
            self.thread.setWorkDirectory(os.path.abspath(activeWindow.model.workDirectory))
            self.thread.setJobName(activeWindow.model.jobName())
            self.thread.start()

            self.process.setWorkingDirectory(os.path.abspath(activeWindow.model.workDirectory))
            self.process.start(*activeWindow.model.abaqusCommand())
            self.process.finished.connect(setOdb)
        except Exception as e:
            QMessageBox.warning(self, 'Warning', repr(e))

    def extractOutput(self):
        activeWindow = self.currentSubWidget()
        if activeWindow is None:
            return
        try:
            self.process.setWorkingDirectory(os.path.abspath(activeWindow.model.workDirectory))
            self.process.start(*activeWindow.model.extractOutputCommand())
        except Exception as e:
            QMessageBox.warning(self, 'Warning', repr(e))

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

        code = activeWindow.ui.fig.defaultHeader() + """
ax = fig.add_subplot(111)
df = pd.read_csv(r'{}')
lines = 0
x, ys = '{}', {}
for y in ys:
    if y not in df.columns:
        continue
    lines += 1
    ax.plot(df[x], df[y], label=y)
if lines > 0:
    ax.legend()
ax.set_xlabel('{}')
ax.set_ylabel('{}')
ax.set_title('{}')
ax.grid()
fig.tight_layout()
""".format(os.path.join(activeWindow.model.absWorkDirectory(), activeWindow.model.data), x, ys, xlabel, ylabel, title)
        activeWindow.ui.fig.setCode(code)
        activeWindow.ui.tabWidget.setCurrentIndex(3)
