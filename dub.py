from unittest import TestCase # Clase para hacer testing

# Se procede a definir lo que falta despues del testing
from typing import List

from comp.token import (
    Token,
    TokenType,
)
from comp.lexer import Lexer

def test_white_spaces() -> None:
    source: str = \
    '''def suma(x + y):
		return x + y'''
    lexer: Lexer = Lexer(source)
    
    tokens: List[List[Token]] = []
    for i in range(15):
        tokens.append(lexer.next_token())

    newtokens = [item for items in tokens for item in items] # Se usa un list comprehension para hacerle flatting a la lista
    
    print(source)
    for i in newtokens:
        print(i)


test_white_spaces()