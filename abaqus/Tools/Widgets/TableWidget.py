import typing

from PyQt5 import QtWidgets, QtCore, QtGui


class TableWidget(QtWidgets.QTableWidget):

    def __init__(self, parent: typing.Optional[QtWidgets.QWidget] = None):
        super().__init__(parent)
        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.onContextMenuRequested)

    def onContextMenuRequested(self):
        contextMenu = QtWidgets.QMenu(self.sender())
        insertRowBeforeAction = QtWidgets.QAction('Insert Row Before', self)
        insertRowAfterAction = QtWidgets.QAction('Insert Row After', self)
        deleteRowAction = QtWidgets.QAction('Delete Row', self)
        sender = self.sender()
        insertRowAfterAction.triggered.connect(lambda: sender.insertRow(sender.currentRow()))
        insertRowBeforeAction.triggered.connect(lambda: sender.insertRow(sender.currentRow() - 1
                                                                         if sender.currentRow() > 0 else 0))
        deleteRowAction.triggered.connect(lambda: sender.removeRow(sender.currentRow()))
        contextMenu.addAction(insertRowAfterAction)
        contextMenu.addAction(insertRowBeforeAction)
        contextMenu.addAction(deleteRowAction)
        contextMenu.exec(QtGui.QCursor.pos())
