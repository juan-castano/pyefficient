#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from numpy import *
import matplotlib.pyplot as plot

class Operaciones(object):

    def __init__(self):
        pass

    def graficar(self, ecuacion=None):
        x = arange(0,10,0.1)
        y = 2*sin(4*x)-x**2+10*x
        # y = object(ecuacion)
        plot.plot(x,y)
        plot.show()



if __name__ == '__main__':
    operaciones = Operaciones()
    operaciones.graficar()