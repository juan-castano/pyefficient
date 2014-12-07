#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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



    tokens = ['NUMBER', 'NAME',]

    literals = ['+', '-', '*', '/', '(', ')', '[', ']']

    # t_PLUS = r'\+'

    t_ignore = ' \t'

    # NUMBERS AND DIGITS
    numbers = r'(\d+(\.\d*)?|\.\d+)'

    # NAMES AND STRING
    nondigit = r'([a-z])'
    strings = r'(' + nondigit + ')+'

    @TOKEN(numbers)
    def t_NUMBER(self, t):
        # r"""(\d+(\.\d*)?|\.\d+)"""
        try:
            t.value = float(t.value)
        except:
            print("No se puede convertir")
        return t

    @TOKEN(nondigit)
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
        ('left', '+'),
    )


    def p_statement(self, p):
        """ statement : expression """
        p[0] = p[1]

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

    def p_error(self, p):
        print("Expresion Ilegal")