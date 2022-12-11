from comp.lexer import Lexer
from comp.token import(
    Token,
    TokenType
)
import os
import subprocess
# Se procede a definir lo que falta despues del testing
from typing import List

EOF_TOKEN: Token = Token(TokenType.EOF, '') # Variable global que nos indica el fin del programa

def leer():
    # filename = 'ProyectoFinal.txt'
    filename = 'ProyectoFinal.txt'
    filename = open(filename, 'r')
    source = ''
    for i in filename: # Extrayendo texto de archivo en un string
        source = source + i
    
    lexer: Lexer = Lexer(source)

    tokens: List[List[Token]] = []
    for i in range(len(source)):
        tokens.append(lexer.next_token())

    newtokens = [item for items in tokens for item in items] # Se usa un list comprehension para hacerle flatting a la lista
    
    # List comprehension para filtrar los tokens ignore
    newtokens = [items for items in newtokens if items.token_type != TokenType.IGNORE]

    print("Código original: \n")
    print(source)
    
    print("\n\n")

    print("Los tokens son: \n")
    for i in newtokens:
        if i.token_type == TokenType.EOF:
            break
        else:
            print(i)