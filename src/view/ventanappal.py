# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana2.ui'
#
# Created: Sat Dec  6 02:20:46 2014
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

# --------------------------------------------- #
#   Agrega los modulos de la carpeta raiz al    #
#   PYTHONPATH                                  #
# --------------------------------------------- #

import sys
sys.path.append("../")

# --------------------------------------------- #

from PyQt4 import QtCore, QtGui
import easygui as gui


from operaciones import Operaciones
from files.File import File


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class MainWindow(object):
    def setupUi(self, MainWindow):
        print("Inicializando Interfaz...")

        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(640, 480)

        # Widget Principal
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        # Area de Texto
        self.plainTextEdit = QtGui.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(310, 20, 321, 371))
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))

        # Caja de Texto Ecuacion Recurrencia
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 80, 261, 23))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))

        # Etiqueta 'Ecuacion de Recurrencia'
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 60, 221, 16))
        self.label.setObjectName(_fromUtf8("label"))

        # Boton 'graficar'
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(500, 400, 100, 24))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        # Boton 'analizar'
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(380, 400, 77, 24))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))

        # Boton 'limpiar'
        self.limpiarTextoButton = QtGui.QPushButton(self.centralwidget)
        self.limpiarTextoButton.setGeometry(QtCore.QRect(260, 400, 80, 24))
        self.limpiarTextoButton.setObjectName(_fromUtf8("limpiarTextoButton"))

        # Widget Barra de Edicion
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuArchivo = QtGui.QMenu(self.menubar)
        self.menuArchivo.setObjectName(_fromUtf8("menuArchivo"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        self.statusbar.showMessage("Listo")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbrir_archivo = QtGui.QAction(MainWindow)
        self.actionAbrir_archivo.setObjectName(_fromUtf8("actionAbrir_archivo"))
        self.actionSalir = QtGui.QAction(MainWindow)
        self.actionSalir.setObjectName(_fromUtf8("actionSalir"))
        self.menuArchivo.addAction(self.actionAbrir_archivo)
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.actionSalir)
        self.menubar.addAction(self.menuArchivo.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.plainTextEdit, self.lineEdit)
        MainWindow.setTabOrder(self.lineEdit, self.limpiarTextoButton)
        MainWindow.setTabOrder(self.limpiarTextoButton, self.pushButton_2)
        MainWindow.setTabOrder(self.pushButton_2, self.pushButton)

        # Eventos Botones
        self.pushButton.clicked.connect(self.graficar)
        self.pushButton_2.clicked.connect(self.mostrarAlgoritmo)
        self.limpiarTextoButton.clicked.connect(lambda: self.plainTextEdit.setPlainText(""))



    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "Ingresar Ecuación de Recurrencia", None))
        self.pushButton.setText(_translate("MainWindow", "Calcular", None))
        self.pushButton_2.setText(_translate("MainWindow", "Graficar", None))
        self.menuArchivo.setTitle(_translate("MainWindow", "Archivo", None))
        self.actionAbrir_archivo.setText(_translate("MainWindow", "Abrir archivo", None))
        self.actionSalir.setText(_translate("MainWindow", "Salir", None))
        self.limpiarTextoButton.setText(_translate("MainWindow", "Limpiar", None))

    def graficar(self):
        print("Graficando")
        operaciones = Operaciones()
        operaciones.graficar()

    def mostrarAlgoritmo(self):

        objArchivo = File()

        archivo = objArchivo.loadFile()

        if (archivo is None):
            gui.msgbox(title="Error", msg="Error al tratar de abrir el archivo: " + archivo)
        else:
            self.plainTextEdit.setPlainText(archivo.read())
        print("Mostrando archivo...")


