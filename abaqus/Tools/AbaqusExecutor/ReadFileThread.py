import os

from PyQt5.QtCore import QThread, pyqtSignal, QObject, QFileInfo, QMutex


class ReadFileThread(QThread):
    work_directory: str = ''
    job_name: str = 'Job-1'
    files: dict[str, str] = {}

    readyReadyFiles = pyqtSignal(object)

    def __init__(self, work_directory: str = '', job_name: str = 'Job-1', parent: QObject = None):
        self.work_directory = work_directory
        self.job_name = job_name
        super().__init__(parent)

    def setWorkDirectory(self, work_directory: str = ''):
        self.work_directory = work_directory

    def setJobName(self, job_name: str = 'Job-1'):
        self.job_name = job_name

    def run(self) -> None:
        mutex = QMutex()
        extensions = ['msg', 'sta', 'log', 'dat'][:2]
        while True:
            mutex.lock()
            for extension in extensions:
                filepath = os.path.join(self.work_directory, '{}.{}'.format(self.job_name, extension))
                if not QFileInfo(filepath).exists():
                    continue
                with open(filepath, 'r') as file:
                    text = file.read()
                    self.files.update({extension: text})
                    file.close()
            mutex.unlock()
            self.readyReadyFiles.emit(self.files)
            self.sleep(1)
