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


class File:

    def __init__(self):
        """ Function doc"""
        pass

    def loadFile(self, dirFile):
        """
        Load a route from indicated file and return
        a File object
        @params: dirFile : String
        @return: File object
        """

        try:
            if (os.path.exists(dirFile)):
                fileInput = open(dirFile)
                return fileInput
            else:
                print("El archivo '%s' NO existe.\n"
                    % (dirFile.split('/')[-1]))
        except (TypeError):
            print("Error al cargar el archivo %s\n"
                % (dirFile.split('/')[-1]))

