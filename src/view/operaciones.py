#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plot


class Operaciones(object):

    def __init__(self):
        pass

    def graficar(self):
        x = np.arange(0,10,0.1)
        y = 2*np.sin(4*x)-x**2+10*x
        plot.plot(x,y)
        plot.show()



if __name__ == '__main__':
    operaciones = Operaciones()
    operaciones.graficar()