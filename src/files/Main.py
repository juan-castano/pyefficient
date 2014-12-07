#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from File import File

def main():
    dirFile = "../../grammar/Grammar.bnf"
    fileObj = File()
    fileIn = fileObj.loadFile(dirFile)
    print(fileIn.read())

if __name__ == '__main__':
    main()
