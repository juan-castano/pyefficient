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

    def test(self, archivo):
        print("Analizador\n")

        try:

            s = archivo
            if (not s):
                # continue
                print("No es un character")

            print(s)
            result = self.parser.parse(s)
            print(result)
        except (EOFError):
            # continue
            print("Fin de línea")
        except (KeyboardInterrupt):
            print("\nSaliendo...\n")
            sys.exit()

        diccionario = { }
        diccionario['funciones'] = self.funciones
        diccionario['names'] = self.names
        diccionario['clases'] = self.clases

        print(self.funciones)
        print(self.names)
        print(self.clases)

        print(self.peor_caso)
        print(self.mejor_caso)

        '''
        while True:
            try:
                """s = input('dato > ')"""

                s = """def funcion()
                    begin
                    34+3
                    end"""



                if (not s):
                    continue
                result = self.parser.parse(s)
                print(result)

            except (EOFError):
                continue
            except (KeyboardInterrupt):
                print("\nSaliendo...\n")
                sys.exit()
        '''


    reserved = {
        'and': 'AND',
        'or': 'OR',
        'True': 'T',
        'False': 'F',
        'not': 'NOT',
        'for': 'FOR',
        'while': 'WHILE',
        'class': 'CLASS',
        'if': 'IF',
        'else': 'ELSE',
    }

    """

    keywords = (

    )
    """

    tokens = (
        'NUMBER', 'NAME', 'LESSTHQ', 'GREATTHQ', 'NOTEQ', 'ASIGN',
        'CALL', 'REPEAT', 'def', 'begin', 'end', 'TO', 'DO', 'UNTIL',
        'THEN',
    )

    tokens = tokens + tuple(reserved.values())
    # tokens = tokens + keywords

    # tokens = keywords + tokens

    literals = ['+', '-', '*', '/', '(', ')', '[', ']', '<', '>', ':']

    t_ASIGN = r'<-'
    t_LESSTHQ = r'<='
    t_GREATTHQ = r'>='
    t_NOTEQ = r'!='

    t_ignore = ' \t'

    # NUMBERS AND DIGITS
    numbers = r'(\d+(\.\d*)?|\.\d+)'

    # NAMES AND STRING
    nondigit = r'([a-zA-Z_])'
    # strings = r'(' + nondigit + ')+' + r'(' + nondigit + ')*'
    # strings = r'[a-zA-Z_][a-zA-Z0-9_]*'
    strings = r'(' + nondigit + ')+' + r'(' + nondigit + ')*'

    @TOKEN(numbers)
    def t_NUMBER(self, t):
        # r"""(\d+(\.\d*)?|\.\d+)"""
        # print("Number")
        try:
            t.value = float(t.value)
        except:
            print("No se puede convertir")
        return t

    # @TOKEN(strings)
    def t_NAME(self, t):
        r'[a-zA-Z_][a-zA-Z0-9_]*'
        t.type = self.reserved.get(t.value, "NAME")
        return t


    """
    def t_ITEMID(self, t):
        t.type = self.reserved.get(t.value, 'ITEMID')
        if t.type == 'ITEMID':
            tval = self.names.get(t.value, '')
            if tval == '':
                self.t_error(t)
            else:
                t.value = tval
        return t
    """

    # def t_BOOLEAN(self, t):


    def t_newline(self, t):
        r'\n+'
        # print("Nueva linea")
        t.lexer.lineno += t.value.count("\n")

    def t_error(self, t):
        # print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)


    precedence = (
        ('nonassoc', '<', '>', 'LESSTHQ', 'GREATTHQ', 'NOTEQ'),
        ('left', '+', '-', '*', '/'),
        ('right', 'UMINUS'),
    )

    """ DIccionarios, Tuplas y Miscelaneos """

    names = { }
    clases = [ ]
    funciones = [ ]

    peor_caso = { }
    mejor_caso = { }


    def p_statement(self, p):
        """ statement : expression
                    | stmnt """
        # print("Expression")
        p[0] = p[1]
        # print(p[1])

    def p_statemnt_asign(self, p):
        """ statement : NAME ASIGN expression """
        # "self.names[p[1]] = p[3]
        # print("Asignando...")
        # print("Asignacion")
        self.names[p[1]] = p[3]
        return ''

    def p_expression_name(self, p):
        "expression : NAME"
        # print("Exp Name")
        try:
            p[0] = self.names[p[1]]
        except LookupError:
            print("Undefined name '%s'" % p[1])
            p[0] = 0


        """if (p[2] == '<-'):
            self.names[p[1]] = p[3]
        else:
            print("No existe el simbolo, no se puede asignar")
        """

    def p_expression_binop(self, p):
        """ expression : expression '+' expression
                        | expression '-' expression
                        | expression '*' expression
                        | expression '/' expression """

        # print("Exp binop")
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
        # print("Exp Number")
        p[0] = p[1]

    def p_expression_grouping(self, p):
        """ expression_grouping : '(' expression ')'
                        | '[' expression ']' 
                        | '(' empty ')' """
        print("Exp grouping")
        p[0] = p[2]


    def p_empty(self, p):
        """ empty : """
        pass

    def p_expression_comparission(self, p):
        """ expression : expression '<' expression
                        | expression '>' expression
                        | expression LESSTHQ expression
                        | expression GREATTHQ expression
                        | expression NOTEQ expression """
        # print("Exp comparission")
        if (p[2] == '<'):
            p[0] = p[1] < p[3]
        elif (p[2] == '>'):
            p[0] = p[1] > p[3]
        elif (p[2] == '<='):
            p[0] = p[1] <= p[3]
        elif (p[2] == '>='):
            p[0] = p[1] < p[3]
        elif (p[2] == '!='):
            p[0] = p[1] != p[3]

    def p_expression_uminus(self, p):
        """ expression : "-" expression %prec UMINUS """
        # print("Exp uminus")
        p[0] = -p[2]

    def p_expression_boolean(self, p):
        """ expression_boolean : expression OR expression
                        | expression AND expression """
        # print("Exp Bool")
        oper = p[2];
        eval_str = "" % (p[1], oper, p[3])
        p[0] = eval(eval_str)

    def p_stmnt_block(self, p):
        """ stmnt_block : begin expression end """

        print("block")
        pass


    def p_stmnt_class(self, p):
        """ stmnt : CLASS NAME stmnt_block """
        print("class")
        pass


    cant_sentencia_for = 0
    def p_stmnt_for(self, p):
        """ stmnt : FOR NAME TO NUMBER DO stmnt_block """
        print("for")
        self.cant_sentencia_for += 1
        self.peor_caso['for'+self.cant_sentencia_for] = 'n'
        self.mejor_caso['for'+self.cant_sentencia_for] = 'n'



    cant_sentencia_while = 0
    def p_stmnt_while(self, p):
        """ stmnt : WHILE '(' expression_boolean ')' DO stmnt_block """
        print("while")
        self.cant_sentencia_while += 1
        self.peor_caso['while'+self.cant_sentencia_while] = 'n'
        self.mejor_caso['while'+self.cant_sentencia_while] = '1'


    cant_sentencia_repeat = 0
    def p_stmnt_repeat(self, p):
        """ stmnt : REPEAT stmnt_block UNTIL '(' expression_boolean ')' """
        print("repeat")
        self.peor_caso['repeat'+self.cant_sentencia_repeat] = 'n'
        self.mejor_caso['repeat'+self.cant_sentencia_repeat] = '1'

    def p_stmnt_if(self, p):
        """ stmnt : IF '(' expression_boolean ')' THEN stmnt_block
                        |  IF '(' expression_boolean ')' THEN stmnt_block ELSE stmnt_block """
        print("if")


    def p_stmnt_call(self, p):
        """ stmnt : CALL NAME '(' expression ')' """
        print("call")


    def p_stmnt_subrutine(self, p):
        """ stmnt : NAME '(' expression ')'  stmnt_block"""
        print("subrutine")


    def p_stmnt_access_atributte(self, p):
        """ """
        print("attibutte")


    """
    def p_expression_if(self, p):
         stmnt : IF expression ':' expression
                        | IF expression ':' expression ELSE expression
        print("if expression")
    """


    def p_stmnt_def(self, p):
        """ stmnt : def NAME expression_grouping stmnt_block """
        print("def function")



    def p_error(self, p):
        if (p):
            print ("Syntax error at '%s'" % (p.value))
            print(p.lexpos)
        else:
            print ("Syntax error at EOF")