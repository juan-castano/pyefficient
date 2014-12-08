#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

from PyQt4 import QtCore, QtGui

from ventanappal import MainWindow


class ShowWindow(QtGui.QMainWindow):

    def __init__(self):
        QtGui.QApplication.__init__(self, None)
        self.ui = MainWindow()
        self.ui.setupUi(self)

def main(argv):
    app = QtGui.QApplication(argv)
    ventana = ShowWindow()
    ventana.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main(sys.argv)