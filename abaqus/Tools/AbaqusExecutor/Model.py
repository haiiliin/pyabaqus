import os
import json


class Model:

    def __init__(self, workDirectory: str = '', modelScript: str = '', input: str = '', user: str = '', odb: str = '',
                 outputScript: str = '', data: str = '', x: str = '', ys=None, xlabel: str = '', ylabel: str = '',
                 title: str = ''):
        self.fileName = ''
        self.command = 'C:\\SIMULIA\\Commands\\abaqus.bat'

        self.workDirectory = workDirectory
        self.modelScript = modelScript
        self.input = input
        self.user = user
        self.odb = odb
        self.outputScript = outputScript
        self.data = data

        self.x = x
        self.ys = [] if ys is None else ys
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.title = title

    def setData(self, workDirectory: str = '', modelScript: str = '', input: str = '', user: str = '', odb: str = '',
                outputScript: str = '', data: str = '', x: str = '', ys=None, xlabel: str = '', ylabel: str = '',
                title: str = '', *args, **kwargs):
        self.workDirectory = workDirectory
        self.modelScript = modelScript
        self.input = input
        self.user = user
        self.odb = odb
        self.outputScript = outputScript
        self.data = data

        self.x = x
        self.ys = [] if ys is None else ys
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.title = title

    def setAbaqusCommand(self, abaqus: str):
        self.command = abaqus

    def save(self, filePath: str = None):
        if filePath is None:
            filePath = self.absFilePath()
        data = {'modelScript': self.modelScript, 'input': self.input,
                'user': self.user, 'odb': self.odb, 'outputScript': self.outputScript, 'data': self.data,
                'x': self.x, 'ys': self.ys, 'xlabel': self.xlabel, 'ylabel': self.ylabel, 'title': self.title}
        with open(filePath, 'w+') as file:
            json.dump(data, file, indent=4)

    def load(self, filePath: str):
        with open(filePath, 'r+') as file:
            data = json.load(file)
            self.setData(**data)
            self.workDirectory = os.path.dirname(filePath)
            self.fileName = os.path.basename(filePath)

    def absWorkDirectory(self) -> str:
        return os.path.abspath(self.workDirectory)

    def absFilePath(self):
        return os.path.join(self.absWorkDirectory(), self.fileName)

    def __setitem__(self, key: str, value):
        if key not in ['workDirectory', 'modelScript', 'input', 'user', 'odb', 'outputScript', 'data']:
            raise KeyError('Key {} not exist'.format(key))
        exec('self.{} = value'.format(key))

    def jobName(self):
        return self.input.split('.')[0]

    def createModelCommand(self):
        arguments = ['cae', '-noGUI', self.modelScript]
        return self.command, arguments

    def abaqusCommand(self):
        options = ['int', 'double']
        arguments = []
        job = inp = self.input.split('.')[0]
        arguments += ['job={}'.format(job), 'input={}'.format(inp)]
        if not self.user == '':
            arguments.append('user={}'.format(self.user))
        arguments += options
        return self.command, arguments

    def extractOutputCommand(self):
        arguments = ['cae', 'database={}'.format(self.odb), 'script={}'.format(self.outputScript)]
        return self.command, arguments
