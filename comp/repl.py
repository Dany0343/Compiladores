# Se importa el código previamente escrito para el correcto funcionamiento
from comp.lexer import Lexer
from comp.token import (
    Token,
    TokenType
)
from typing import List

EOF_TOKEN: Token = Token(TokenType.EOF, '') # Variable global que nos indica el fin de la oracion
tokens: List[List[Token]] = []
newTokens: List[Token] = []

def start_repl() -> None:   # Aquí no tenemos self como parametro ya que es una función global, no pertenece a una clase, no regresa nada

    # Walrus Operator permite generar una asignación al mismo tiempo que se puede generar algún tipo de chequeo dentro de esta variable que se comienza a asignar, muy util dentro de while loops, for loops
    while (source := input('>> ')) != 'salir()':
        lexer: Lexer = Lexer(source)

        while (token := lexer.next_token()):
            tokens.append(token)
        
        flat_list = flatting(tokens)

        while (token := lexer.next_token()) != EOF_TOKEN:
            print(flat_list[i])
            i += 1


def flatting(tokens) -> List[Token]:
    flat_list = []
    for element in tokens:
        if type(element) is List:
            for item in element:
                flat_list.append(item)
        else:
            flat_list.append(element)
    return flat_list