__author__ = "maciek"

from PyQt5 import QtGui, QtCore
from analyzer import Analyzer

app = QtGui.QApplication([])


# Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == "__main__":
    import sys

    analyzer = Analyzer()
    analyzer.show()

    if (sys.flags.interactive != 1) or not hasattr(QtCore, "PYQT_VERSION"):
        QtGui.QApplication.instance().exec_()
