import typing
from enum import IntEnum
from io import BytesIO

import matplotlib
import matplotlib.pyplot as plt
from PyQt5.QtCore import QSize, QFileInfo
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QMessageBox, QLabel
from matplotlib.axes import Axes
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure

plt.rc('mathtext', fontset='cm')


# matplotlib.rcParams['text.usetex'] = True
# matplotlib.rcParams['text.latex.unicode'] = True
# matplotlib.rcParams['text.latex.preamble'] = [r'\usepackage{CJK}',
#                                               r'\AtBeginDocument{\begin{CJK}{UTF8}{gbsn}}',
#                                               r'\AtEndDocument{\end{CJK}}']


class DisplayRole(IntEnum):
    Text = 0
    Equation = 1


class QTeXWidget(QLabel):
    m_TeX: str = ''
    filename: str = ''
    role = DisplayRole.Text

    @typing.overload
    def __init__(self, parent=None):
        pass

    @typing.overload
    def __init__(self, text='', filename='', parent=None):
        pass

    def __init__(self, *args):
        if len(args) == 0:
            text, parent = '', None
        elif type(args[0]) == str:
            text, parent = args[0], args[1] if len(args) == 2 else None
        else:
            text, parent = '', args[0] if len(args) == 1 else None
        super().__init__(parent)
        self.setText(text)

    def setText(self, TeX: str, role=DisplayRole.Text, useTeX=False, fontsize=10, filename=None):
        self.m_TeX = TeX
        self.role = role
        if filename is not None:
            self.filename = filename
        self.update(useTeX=useTeX, fontsize=fontsize)

    def text(self):
        return self.m_TeX

    def setDisplayRole(self, role=DisplayRole.Text):
        self.role = role

    def displayRole(self) -> DisplayRole:
        return self.role

    def update(self, useTeX=False, fontsize=10):
        try:
            if QFileInfo('Cache/{filename}.png'.format(filename=self.filename)).exists():
                pixmap = QPixmap()
                pixmap.load('Cache/{filename}.png'.format(filename=self.filename), format='PNG')
                self.setPixmap(pixmap)
            else:
                pixmap = self.TeX2Pixmap(self.m_TeX, fontsize=fontsize, size=self.size(), useTeX=useTeX)
                self.setPixmap(pixmap)
                pixmap.save('Cache/{filename}.png'.format(filename=self.filename), format='PNG', quality=100)
            self.setAlignment(self.alignment())
        except Exception as e:
            QMessageBox.warning(self, 'Warning', repr(e))
            return

    @staticmethod
    def TeX2svg(formula, fontsize=15, dpi=300, useTeX=False):
        # https://gist.github.com/gmarull/dcc8218385014559c1ca46047457c364#file-example-TeX2svg-py
        """Render TeX formula to SVG.
        Args:
            formula (str): TeX formula.
            fontsize (int, optional): Font size.
            dpi (int, optional): DPI.
            useTeX (bool, optional): use TeX or not.
        Returns:
            str: SVG render.
        """

        matplotlib.rcParams['text.usetex'] = useTeX
        fig: Figure = plt.figure()
        fig.text(0, 0, formula, fontsize=fontsize, wrap=True, fontname='Times New Roman')

        output = BytesIO()
        fig.savefig(output, dpi=dpi, transparent=True, format='svg',
                    bbox_inches='tight', pad_inches=0.0, frameon=False)
        plt.close(fig)

        output.seek(0)
        return output.read()

    @staticmethod
    def TeX2Pixmap(text, fontsize=20, size=QSize(500, 300), dpi=100, useTeX=False) -> QPixmap:
        # https://stackoverflow.com/questions/32035251/displaying-laTeX-in-pyqt-pyside-qtablewidget
        # ---- set up a mpl figure instance ----
        matplotlib.rcParams['text.usetex'] = useTeX

        fig: Figure = plt.figure(figsize=(size.width() / dpi, size.height() / dpi), dpi=dpi)
        fig.patch.set_facecolor('none')
        fig.set_canvas(FigureCanvasAgg(fig))
        renderer = fig.canvas.get_renderer()

        # ---- plot the mathTex expression ----

        ax: Axes = fig.add_axes([0, 0, 1, 1])
        ax.axis('off')
        ax.patch.set_facecolor('none')
        t = ax.text(0, 0, text, ha='left', va='bottom', fontsize=fontsize, wrap=True)

        # ---- fit figure size to text artist ----

        width, height = fig.get_size_inches()

        fig_bbox = fig.get_window_extent(renderer)

        text_bbox = t.get_window_extent(renderer)

        tight_width = text_bbox.width * width / fig_bbox.width
        tight_height = text_bbox.height * height / fig_bbox.height

        fig.set_size_inches(tight_width, tight_height)

        # ---- convert mpl figure to QPixmap ----

        buf, size = fig.canvas.print_to_buffer()
        image = QImage.rgbSwapped(QImage(buf, size[0], size[1], QImage.Format_ARGB32))
        pixmap = QPixmap(image)

        plt.close()

        return pixmap
