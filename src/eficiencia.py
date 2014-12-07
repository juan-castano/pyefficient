'''
Created on 14/11/2014

@author: juan
'''

from math import log
from builtins import range


class Eficiencia(object):
    '''
    classdocs
    '''

    def __init__(self, params):
        '''
        Constructor
        '''
        
    def calcular_complejidad_recursiva(self, cadena):
                
        lista = cadena.split() # Separar ecuacion
                
        # ['2T','n', '2', 'f(n)']
        a = float(lista[0][0])
        b = float(lista[2])
        n = lista[-1]
        
        # Epsilon
        k = float(range(0,1))
        
        # Metodo 1
        metodo1 = "n^log( b(a) )"
        
        x = log(a,b)-k
        
        # pow(base, exponente)
        if (n <= pow(n,x)):
            return ("Tetta(n) = %s" % (metodo1))
        
        
        # Metodo 2
        metodo2 = "log(n)*n^(log(b,(a)))"
        x = log(a,b)
        
        if (n == pow(n,x)):
            return ("Tetta(n) = %s" % (metodo2))
        
        # Metodo 3
        metodo3 = "f(n)"
        x = log(a,b) + k
        
        # Constante
        c = float(range(0,1))
        
        if (n >= pow(n,x)):
            if (a*(n/b) <= c*n):
                return ("Tetta(n) = %s" % (metodo3))
        