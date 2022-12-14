# Se van a importar varias cosas
from enum import (
    auto, # Permite que automaticamente se asigne un valor al enum
    Enum, # Se trae clase Enum
    unique, # Decorador el cual permite definir que los enums son unicos
)
from typing import ( # Se importa Dict tambien
    Dict,
    NamedTuple
)

@unique # Se le añade el decorador unique pora saber que los tokens son unicos, un decorador recibe como parametro una funcion, le añade cosas, la ejecuta y retorna a esta misma función pero ya modificada, por eso se dice que retorna una función diferente
class TokenType(Enum):
    # Es buena practica ponerlos en orden alfabetico
    # auto es que no interesa el valor del enum
    ASSIGN = auto()
    APPEND = auto()
    COMMA = auto()
    COLON = auto()
    COMMENT = auto()
    DIV = auto()
    DEDENT = auto() 
    DOT = auto()
    DQUOTE = auto()
    ELSE = auto()
    EOF = auto()
    EQ = auto() # '=='
    EXC = auto() # '!'
    FALSE = auto()
    FOR = auto()
    FUNCTION = auto()
    GT = auto() # '>'
    IDENT = auto()
    INDENT = auto() 
    IF = auto()
    ILLEGAL = auto()
    IGNORE = auto()
    IN = auto()
    INT = auto()
    INPUT = auto()
    INTW = auto()
    LPAREN = auto()
    LEN = auto()
    LT = auto() # <
    LB = auto() # [
    MINUS = auto()
    MULT = auto()
    NOT_EQ = auto()
    NEWLINE = auto()
    PLUS = auto()
    PRINT = auto()
    RANGE = auto()
    RETURN = auto()
    RPAREN = auto()
    RB = auto() # ]
    SEMICOLON = auto()
    SQUOTE = auto()
    SPACE = auto()
    TRUE = auto()


class Token(NamedTuple):
    token_type: TokenType
    literal: str

    # Dounder method string que permite saber cuando se imprime el token que hay dentro
    # __str__ permite controlar la funcion global o el built-in function str
    # En python se pueden controlar que es lo que hace el simbolo de suma, len, comparaciones, todos con dounder methods, en este caso cuando queramos imprimir un objeto de tipo Token podemos modificar el como queremos verlo
    # def __str__(self) -> str: # La flecha significa en el mundo de typing de python que esta función va a regresar un string
    #     return f'Type: {self.token_type}, Literal: {self.literal}'


# Funcion para leer palabras más complejas y no solo operadores
def lookup_token_type(literal: str) -> TokenType: # Recibe una literal y regresa un TokenType
    keywords: Dict[str, TokenType] = { # Guarda los keyword del lenguaje de llaves strings y valores TokenType, se escriben en orden alfabetico
        'False': TokenType.FALSE,
        'def': TokenType.FUNCTION,
        'return': TokenType.RETURN,
        'if': TokenType.IF,
        'else': TokenType.ELSE,
        'True': TokenType.TRUE,
        'for': TokenType.FOR,
        'in': TokenType.IN,
        'print': TokenType.PRINT,
        'range': TokenType.RANGE,
        'int': TokenType.INTW,
        'input': TokenType.INPUT,
        'append': TokenType.APPEND,
        'len': TokenType.LEN,
    } 

    return keywords.get(literal, TokenType.IDENT) # Aqui revisa si es una llave de la lista de palabras reservadas que tenemos en el diccionario o si no es un identificador (para nombrar algo y a libre eleccion)
    # En .get el segundo parametro es: Optional. A value to return if the specified key does not exist Default value None