import os
import sys
from threading import Thread

from PyQt5.QtWidgets import QApplication, QStyle

from .Mdb.Mdb import Mdb as AbaqusMdb
from .Session.Session import Session
from .Tools.JobMonitor.JobMonitor import JobMonitor


class Mdb(AbaqusMdb):

    def __init__(self, pathName: str = ''):
        super().__init__(pathName)

    def save(self):
        super().save()

    def saveAs(self, pathName: str):
        abaqus = 'abaqus'
        if 'ABAQUS_BAT_SETTING' in os.environ.keys():
            abaqus = os.environ['ABAQUS_BAT_PATH']
        os.system('{} cae -noGUI {}'.format(abaqus, os.path.abspath(sys.argv[0])))


session = Session()
mdb = Mdb()


def runPythonScript(scriptPath: str):
    """

    Parameters
    ----------
    scriptPath: str
        File path of the python script

    Returns
    -------
    None
    """
    abaqus = 'abaqus'
    if 'ABAQUS_BAT_SETTING' in os.environ.keys():
        abaqus = os.environ['ABAQUS_BAT_PATH']
    os.chdir(os.path.dirname(os.path.abspath(scriptPath)))
    os.system('{} cae noGUI={}'.format(abaqus, scriptPath))


def extractOutputData(odb: str, script: str):
    """Extract output data using python script

    Parameters
    ----------
    odb: str
        File path of the output database
    script: str
        File path of the script

    Returns
    -------
    None
    """
    abaqus = 'abaqus'
    if 'ABAQUS_BAT_SETTING' in os.environ.keys():
        abaqus = os.environ['ABAQUS_BAT_PATH']
    os.system('{} cae database={} script={}'.format(abaqus, os.path.abspath(odb), os.path.abspath(script)))


def submitJobByInputFile(inputFile: str, userSubroutine: str = None, options: str = 'int', showStatus: bool = True):
    """Submit job by input file, can not execute in Python environment of Abaqus

    Parameters
    ----------
    inputFile: str
        File path of the input file, suffix can be included or not.
    userSubroutine: str
        File path of the user-defined subroutine, if the file is in the directory of the input file, in this way
        this variable should be file name of the subroutine (otr the whole file path if you want), if the file is not
        in the directory of the input file, this variable should be the whole file path.
        whole
    options: str
        Command options for abaqus command, see https://help.3ds.com/2022/english/dssimulia_established/SIMACAEEXCRefMap/simaexc-c-analysisproc.htm?contextscope=all&id=b034a4baa38a4e9496fce622201c4e30
        or https://abaqus-docs.mit.edu/2017/English/SIMACAEEXCRefMap/simaexc-c-analysisproc.htm
        for details, job or input options shouldn't be included, i.e. `int double'.
    showStatus: bool
        Show status or not when the calculation starts.

    Returns
    -------
    None
    """
    abaqus = 'abaqus'
    if 'ABAQUS_BAT_SETTING' in os.environ.keys():
        abaqus = os.environ['ABAQUS_BAT_PATH']
    absInputFilePath = os.path.abspath(inputFile)
    workDirectory = os.path.dirname(absInputFilePath)
    jobName = os.path.basename(absInputFilePath.replace('.inp', ''))

    if showStatus:
        monitorThread = Thread(target=_jobMonitor, args=(workDirectory, jobName))
        monitorThread.start()
    abaqusThread = Thread(target=_runAbaqus, args=(userSubroutine, abaqus, workDirectory, jobName, options))
    abaqusThread.start()


def _runAbaqus(userSubroutine: str, abaqus: str, workDirectory: str, jobName: str, options: str):
    if userSubroutine is not None:
        commandLine = "{} job={} user={} {}".format(abaqus, jobName, userSubroutine, options)
    else:
        commandLine = "{} job={} {}".format(abaqus, jobName, options)
    os.system('cd {}'.format(workDirectory))
    os.system(commandLine)


def _jobMonitor(workDirectory: str, jobName: str):
    app = QApplication(sys.argv)
    monitor = JobMonitor()
    monitor.setWindowIcon(QApplication.style().standardIcon(QStyle.SP_TitleBarMenuButton))
    monitor.setWorkDirectory(workDirectory)
    monitor.setJobName(jobName)
    monitor.show()
    monitor.run()
    sys.exit(app.exec_())
