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

import easygui as gui

class File:

    def __init__(self):
        """ Function doc"""
        pass

    def loadFile(self):
        """
        Load a route from indicated file and return
        a File object
        @params: dirFile : String
        @return: File object
        """

        print("Cargando archivo...")
        extensiones = ['*.py', '*.txt']
        archivo = gui.fileopenbox(title="Abrir Algoritmo",filetypes=extensiones)

        try:
            archivo = open(archivo, 'r')
            return archivo
        except (FileExistsError, FileNotFoundError):
            return None


