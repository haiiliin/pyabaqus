from matplotlib.backends.backend_qt5agg import \
    FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from pyqtconsole.console import PythonConsole
from pyqtconsole.console import PythonInterpreter
from pyqtconsole.interpreter import redirected_io


class MatplotlibPythonInterpreter(PythonInterpreter):
    figure: Figure
    canvas: FigureCanvas

    def __init__(self, stdin, stdout, locals):
        PythonInterpreter.__init__(self, stdin, stdout, locals=locals)

    def exec(self, codes):
        self._executing = True
        result = None

        # Redirect IO and disable excepthook, this is the only place were we
        # redirect IO, since we don't how IO is handled within the code we
        # are running. Same thing for the except hook, we don't know what the
        # user are doing in it.
        try:
            with redirected_io(self.stdout):
                for code, mode in codes:
                    if mode == 'eval':
                        result = eval(code)
                    else:
                        exec(code)
        except SystemExit as e:
            self.exit_signal.emit(e)
        except BaseException:
            self.showtraceback()
        finally:
            self._executing = False
            self.done_signal.emit(True, result)


class MatplotlibPythonConsole(PythonConsole):
    def __init__(self, parent=None, locals=None, formats=None):
        PythonConsole.__init__(self, parent, locals=locals, formats=formats)
        self.interpreter = MatplotlibPythonInterpreter(
            self.stdin, self.stdout, locals=locals)
        self.interpreter.done_signal.connect(self._finish_command)
        self.interpreter.exit_signal.connect(self.exit)

    def runsouurce(self, source: str, filename="<input>", symbol="multi"):
        try:
            codes = self.interpreter.compile(source, filename, symbol)
        except (OverflowError, SyntaxError, ValueError):
            # Case 1
            self.interpreter.showsyntaxerror(filename)
            return False
        if codes is None:
            # Case 2
            return True
        try:
            self.interpreter.exec(codes)
            pass
        except SystemExit:
            raise
        except:
            self.interpreter.showtraceback()
        return False
