# Se importa el código previamente escrito para el correcto funcionamiento
from comp.lexer import Lexer
from comp.token import (
    Token,
    TokenType
)
from typing import List
import subprocess

EOF_TOKEN: Token = Token(TokenType.EOF, '') # Variable global que nos indica el fin de la oracion
tokens: List[List[Token]] = []
newTokens: List[Token] = []

def start_repl() -> None:   # Aquí no tenemos self como parametro ya que es una función global, no pertenece a una clase, no regresa nada
    print("Escriba salir() para salir al menu")
    # Walrus Operator permite generar una asignación al mismo tiempo que se puede generar algún tipo de chequeo dentro de esta variable que se comienza a asignar, muy util dentro de while loops, for loops
    while (source := input('>> ')) != 'salir()':
        lexer: Lexer = Lexer(source)

        tokens: List[List[Token]] = []
        for i in range(len(source)):
            tokens.append(lexer.next_token())

        newtokens = [item for items in tokens for item in items] # Se usa un list comprehension para hacerle flatting a la lista
        # List comprehension para filtrar los tokens ignore
        newtokens = [items for items in newtokens if items.token_type != TokenType.IGNORE]

        for i in newtokens:
            if i.token_type == TokenType.EOF:
                break
            else:
                print(i)
                print("Se parsea")
                print("\n\nAhora parseandolo tenemos\n")
                print("En construcción... :c")
                # subprocess.call("python3 parser2.py test.py", shell=True)