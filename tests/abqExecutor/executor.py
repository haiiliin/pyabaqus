from PyQt5.QtCore import QSettings
from PyQt5.QtWidgets import QApplication

import abaqus

def registerFileRelation():
    className = "AbaqusExecutor"
    appPath = QApplication.applicationFilePath()
    ext = ".abqjson"
    extDes = "Abaqus Executor File"
    baseUrl = "HKEY_CURRENT_USER\\Software\\Classes"
    setting = QSettings(baseUrl, QSettings.NativeFormat)
    setting.setValue("/" + className + "/Shell/Open/Command/.", "\"" + appPath + "\" \"%1\"")
    setting.setValue("/" + className + "/.", extDes)
    setting.setValue("/" + className + "/DefaultIcon/.", appPath + ",0")
    setting.setValue("/" + ext + "/OpenWithProgIds/" + className, "")
    setting.sync()

registerFileRelation()
abaqus.executor()
