import os
import sys

from .Mdb.Mdb import Mdb as BaseMdb
from .Session.Session import Session


class Mdb(BaseMdb):

    def __init__(self, pathName: str = ''):
        super().__init__(pathName)
        self.abaqus_bat_path = None
        self.abaqus_bat_setting = None
        self.debug = None

    def saveAs(self, pathName: str):
        if isinstance(self.debug, bool) and self.debug:
            print(pathName)
        if 'ABAQUS_BAT_SETTING' in os.environ.keys():
            self.abaqus_bat_path = os.environ['ABAQUS_BAT_PATH']
        if 'ABAQUS_BAT_PATH' in os.environ.keys():
            self.abaqus_bat_setting = os.environ['ABAQUS_BAT_SETTING']
        os.system('{} cae -{} {}'.format(self.abaqus_bat_path, self.abaqus_bat_setting, os.path.abspath(sys.argv[0])))

    def submitInputFile(self, inputFile: str, options: str = 'int', showStatus: bool = True):
        absInputFilepath = os.path.abspath(inputFile)
        os.system('cd {}'.format(os.path.dirname(absInputFilepath)))
        if showStatus is True:
            staFile = os.path.basename(absInputFilepath.replace('.inp', '')) + '.sta'
            if not os.path.exists(staFile):
                with open(staFile, 'w+') as f:
                    f.write('')
                    f.close()
            os.startfile(staFile)
        os.system("{} job={} {}".format(self.abaqus_bat_path, os.path.basename(absInputFilepath.replace('.inp', '')), options))


session = Session()
mdb = Mdb()
