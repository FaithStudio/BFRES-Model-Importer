

import sys
from PyQt4 import QtGui
from mainWindow import MainWindow


def main():
    app = QtGui.QApplication (sys.argv)
    m = MainWindow ()
    m.show ()
    sys.exit (app.exec_ () )


if __name__ == '__main__':
    main ()