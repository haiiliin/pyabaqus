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


session = Session()
mdb = Mdb()


def submitJobByInputFile(inputFile: str, userSubroutine: str = None, options: str = 'int', showStatusFile: bool = True,
                         abaqus: str = 'abaqus'):
    """Submit job by input file

    Parameters
    ----------
    inputFile
        File path of the input file, suffix can be included or not.
    userSubroutine
        File path of the user-defined subroutine, if the file is in the directory of the input file, in this way
        this variable should be file name of the subroutine (otr the whole file path if you want), if the file is not
        in the directory of the input file, this variable should be the whole file path.
        whole
    options
        Command options for abaqus command, see https://help.3ds.com/2022/english/dssimulia_established/SIMACAEEXCRefMap/simaexc-c-analysisproc.htm?contextscope=all&id=b034a4baa38a4e9496fce622201c4e30
        or https://abaqus-docs.mit.edu/2017/English/SIMACAEEXCRefMap/simaexc-c-analysisproc.htm
        for details, job or input options shouldn't be included, i.e. `int double'.
    showStatusFile
        Show status file (.sta) or not when the calculation starts.
    abaqus
        File path of the abaqus command, if the folder contains abaqus commands is added to the system variables, you
        omit the file directory, i.e., just `abaqus`.

    Returns
    -------
    None
    """
    absInputFilepath = os.path.abspath(inputFile)
    workDirectory = os.path.dirname(absInputFilepath)
    if showStatusFile is True:
        staFile = os.path.basename(absInputFilepath.replace('.inp', '')) + '.sta'
        if not os.path.exists(staFile):
            with open(staFile, 'w+') as f:
                f.write('')
                f.close()
        os.startfile(staFile)
    if userSubroutine is not None:
        commandLine = "{} job={} user={} {}".format(abaqus, os.path.basename(absInputFilepath.replace('.inp', '')),
                                                    userSubroutine, options)
    else:
        commandLine = "{} job={} {}".format(abaqus, os.path.basename(absInputFilepath.replace('.inp', '')), options)
    os.system('cd {}'.format(workDirectory))
    os.system(commandLine)
