#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#
#    File: Rules.py
#    Date: Oct 27 - 2014 - 10:54 AM GMT-5
#    Location: Manizales, Caldas - Colombia
#    Author: Juan Camilo Castaño Serna
#    Description: This file define the File class
#

import os
import sys

# import easygui as gui

from PyQt4 import QtGui, QtCore

class File(QtGui.QMainWindow):

    def __init__(self):
        """ Function doc"""
        QtGui.QMainWindow.__init__(self)

    def loadFile(self):
        """
        Load a route from indicated file and return
        a File object
        @params: dirFile : String
        @return: File object
        """

        print("Cargando archivo...")

        try:
            archivo = QtGui.QFileDialog.getOpenFileName(self, 'Abrir Algoritmo', '/home/juan')
            print (archivo)
            archivo = open(archivo, 'r')
            return archivo
        except (FileExistsError, FileNotFoundError):
            return None


