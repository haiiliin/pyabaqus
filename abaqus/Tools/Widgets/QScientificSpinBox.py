from PyQt5.QtWidgets import QDoubleSpinBox


class QScientificSpinBox(QDoubleSpinBox):

    def __init__(self, parent=None):
        super(QScientificSpinBox, self).__init__(parent)
        self.setDecimals(10)
        self.setMinimum(float('-inf'))
        self.setMaximum(float('inf'))

    def textFromValue(self, v: float) -> str:
        return '{:.1e}'.format(v)
