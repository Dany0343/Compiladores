import ast
import json
from ast import parse
from ast2json import ast2json

def astGen(code):
    tree = ast.parse(code)

    # Se procede a dumpear para poder verlo en formato de texto
    '''
    .dump es una función del módulo ast de la biblioteca estándar de Python que se usa para imprimir una representación en formato de texto de un árbol de sintaxis abstracta (AST, por sus siglas en inglés). El AST es una representación en formato de árbol del código fuente en un lenguaje de programación, que se puede manipular y analizar fácilmente por programas.

    La función ast.dump toma un objeto del AST como su único argumento y devuelve una cadena de texto que contiene una representación detallada del AST en formato de texto. Esta función es útil para imprimir el AST en la consola o para guardarlo en un archivo para su posterior análisis.
    '''
    print(ast.dump(tree))


def jsonAst(code):
    ast = ast2json(parse(open('ProyectoFinal.txt').read()))
    print(json.dumps(ast, indent=4))