import os

from PyQt5.QtCore import QThread, pyqtSignal


class FileMonitorThread(QThread):
    readyReadStatusFile = pyqtSignal(object)
    readyReadMessageFile = pyqtSignal(object)
    readyReadCmdText = pyqtSignal(object)

    def __init__(self, workDirectory='', jobName=''):
        super().__init__()
        self.workDirectory = workDirectory
        self.jobName = jobName
        self.statusFilePath = ''
        self.messageFilePath = ''

    def setWorkDirectory(self, workDirectory: str):
        self.workDirectory = workDirectory
        self.generateFilePaths()

    def setJobName(self, jobName: str):
        self.jobName = jobName
        self.generateFilePaths()

    def generateFilePaths(self):
        self.statusFilePath = os.path.join(self.workDirectory, self.jobName) + '.sta'
        self.messageFilePath = os.path.join(self.workDirectory, self.jobName) + '.msg'

    def run(self) -> None:
        while True:
            if not os.path.exists(self.statusFilePath):
                self.readyReadStatusFile.emit('')
            else:
                with open(self.statusFilePath, 'r') as file:
                    text = file.read()
                    self.readyReadStatusFile.emit(text)
                    file.close()

            if not os.path.exists(self.messageFilePath):
                self.readyReadMessageFile.emit('')
            else:
                with open(self.messageFilePath, 'r') as file:
                    text = file.read()
                    self.readyReadMessageFile.emit(text)
                    file.close()

            self.sleep(1)
