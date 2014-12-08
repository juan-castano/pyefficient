#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

import ply.lex as lex
import ply.yacc as yacc
from ply.lex import TOKEN

class Analizador(object):

    def __init__(self):
        self.lexer = lex.lex(module=self)
        self.parser = yacc.yacc(module=self)

    def test(self):
        print("Analizador\n")

        while True:
            try:
                s = input('dato > ')

                if (not s):
                    continue
                result = self.parser.parse(s)
                print(result)

            except (EOFError):
                continue
            except (KeyboardInterrupt):
                print("\nSaliendo...\n")
                sys.exit()

    reserved = {
        'and': 'AND',
        'or': 'OR',
        'True': 'T',
        'False': 'F',
        'not': 'NOT',
    }

    tokens = ['NUMBER', 'NAME', 'LESSTHQ', 'GREATTHQ', 'NONEQ', 'ASIGN']

    literals = ['+', '-', '*', '/', '(', ')', '[', ']', '<', '>']

    t_ASIGN = '<-'
    t_LESSTHQ = r'<='
    t_GREATTHQ = r'>='
    t_NONEQ = r'!='

    t_ignore = ' \t'

    # NUMBERS AND DIGITS
    numbers = r'(\d+(\.\d*)?|\.\d+)'

    # NAMES AND STRING
    nondigit = r'([a-z])'
    strings = r'(' + nondigit + ')+' + r'(' + nondigit + ')*'

    @TOKEN(numbers)
    def t_NUMBER(self, t):
        # r"""(\d+(\.\d*)?|\.\d+)"""
        try:
            t.value = float(t.value)
        except:
            print("No se puede convertir")
        return t

    @TOKEN(strings)
    def t_NAME(self, t):
        t.value = self.reserved.get(t.value, 'NAME')
        return t

    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += t.value.count("\n")

    def t_error(self, t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)


    precedence = (
        ('nonassoc', '<', '>', 'LESSTHQ', 'GREATTHQ'),
        ('left', '+', '-', '*', '/'),
        ('right', 'UMINUS'),
    )

    names = { }

    def p_statement(self, p):
        """ statement : expression """
        p[0] = p[1]
        # print(p[1])

    def p_expression_asign(self, p):
        """ expression : NAME ASIGN expression """
        if (p[2] == '<-'):
            self.names[p[1]] = p[3]
        else:
            print("No existe el simbolo, no se puede asignar")

    def p_expression_binop(self, p):
        """ expression : expression '+' expression
                        | expression '-' expression
                        | expression '*' expression
                        | expression '/' expression """

        if (p[2] == '+'):
            p[0] = p[1] + p[3]
        elif (p[2] == '-'):
            p[0] = p[1] - p[3]
        elif (p[2] == '*'):
            p[0] = p[1] * p[3]
        elif (p[2] == '/'):
            if (p[3] == 0):
                print("No se puede dividir por CERO")
                p[0] = 0.0
            else:
                p[0] = p[1] / p[3]


        # p[0] = p[1] + p[3]

    def p_expression_number(self, p):
        """ expression : NUMBER """
        p[0] = p[1]

    def p_expression_grouping(self, p):
        """ expression : '(' expression ')'
                        | '[' expression ']' """
        p[0] = p[2]

    def p_expression_boolean(self, p):
        """ expression : expression '<' expression
                        | expression '>' expression
                        | expression LESSTHQ expression
                        | expression GREATTHQ expression
                        | expression NONEQ expression """

        if (p[2] == '<'):
            p[0] = p[1] < p[3]
        elif (p[2] == '>'):
            p[0] = p[1] > p[3]
        elif (p[2] == '<='):
            p[0] = p[1] <= p[3]
        elif (p[2] == '>='):
            p[0] = p[1] < p[3]

    def p_expression_uminus(self, p):
        """ expression : "-" expression %prec UMINUS """
        p[0] = -p[2]


    def p_error(self, p):
        if (p):
            print ("Syntax error at '%s'" % (p.value))
        else:
            print ("Syntax error at EOF")