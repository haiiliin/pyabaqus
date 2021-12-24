import os
import sys

from .Session import Session
from .Mdb import Mdb as BaseMdb


class Mdb(BaseMdb):

    def __init__(self, pathName: str = ''):
        super().__init__(pathName)
        self.abaqus_bat_path = os.environ['ABAQUS_BAT_PATH']
        self.abaqus_bat_setting = os.environ['ABAQUS_BAT_SETTING']
        self.debug = None

    def saveAs(self, pathName: str):
        if isinstance(self.debug, bool) and self.debug:
            print(pathName)
        if 'ABAQUS_BAT_SETTING' in os.environ.keys():
            self.abaqus_bat_path = os.environ['ABAQUS_BAT_PATH']
        if 'ABAQUS_BAT_PATH' in os.environ.keys():
            self.abaqus_bat_setting = os.environ['ABAQUS_BAT_SETTING']
        os.system(self.abaqus_bat_path + ' cae -' + self.abaqus_bat_setting + ' ' + os.path.abspath(sys.argv[0]))

session = Session()
mdb = Mdb()
