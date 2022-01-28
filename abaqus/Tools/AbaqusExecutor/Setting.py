import os

from PyQt5.QtCore import QSettings


class Setting(dict):

    def __init__(self):
        super().__init__()
        self['abaqus'] = ''
        self.detectAbaqusCommand()

    def detectAbaqusCommand(self):
        self['abaqus'] = ''
        paths = os.environ['Path'].split(';')

        setting = QSettings('AbaqusExecutor', 'Configuration')
        self['abaqus'] = setting.value('abaqus') if setting.value('abaqus') is not None else ''
        if os.path.exists(self['abaqus']) and self['abaqus'].endswith('.bat'):
            return
        
        for path in paths:
            if 'abaqus' not in path and 'SIMULIA' not in path:
                continue
            files = os.listdir(path)
            for file in files:
                if ('abaqus' in file or 'abq' in file) and file.endswith('.bat'):
                    self['abaqus'] = os.path.join(path, file)
                    return

    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        if key == 'abaqus':
            self.saveAbaqusCommand2Registry()

    def saveAbaqusCommand2Registry(self):
        setting = QSettings('AbaqusExecutor', 'Configuration')
        if os.path.exists(self['abaqus']) and self['abaqus'].endswith('.bat') and not self['abaqus'] == setting.value('abaqus'):
            setting.setValue('abaqus', self['abaqus'])
