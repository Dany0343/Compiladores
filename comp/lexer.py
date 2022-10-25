from re import match
from comp.token import (
    Token,
    TokenType,
    lookup_token_type,
)
from typing import List


class Lexer:
    def __init__(self, source: str) -> None: # Constructor

        # Se inicializan variables privadas
        self._source: str = source
        self._character: str = ''
        self._read_position: int = 0
        self._position: int = 0
        self._indents = [0]
        self._firts_dedent_flag = True
        # Cuando se inicializa se necesita correr por primera vez para que los caracteres se pongan correctamente
        self._read_character()


    def next_token(self) -> List[Token]:

        # Se va a revisar con expresiones regulares
        """
        En Python las expresiones regulares empiezan con cadenas row
        Comience al principio de la cadena, encuentre un igual y que termine en esto, se quiere un igual desde el principio hasta el final
        """
        self._skipSpaces() # Se ignorara la tokenizacion de los espacios en blanco aun cuando hay un token especial asignado a ello
        if match(r'^=$', self._character):
            if self._peek_character() == '=':
                token = self._make_two_character_token(TokenType.EQ)
            else: 
                token = [Token(TokenType.ASSIGN, self._character)]
        elif match(r'^\+$', self._character):  # Se escapa por tener un significado especial en las expresiones regulares
            token = [Token(TokenType.PLUS, self._character)]
        elif match(r'^\n$', self._character):
            # if len(self._indents) == 2 and self._firts_dedent_flag == False:
            #     if len(self._indents) == 2 and self._indents[1] == 1:
            #         self._firts_dedent_flag = True
            #         token = [Token(TokenType.NEWLINE, self._character), Token(TokenType.DEDENT, self._read_position)]
            #     else:
            #         token = [Token(TokenType.NEWLINE, self._character)]
            # else:
                token = [Token(TokenType.NEWLINE, self._character)]
        elif match(r'^$', self._character):
            token = [Token(TokenType.EOF, self._character)]
        elif match(r'^\($', self._character): # Se escapa por tener un significado especial en las expresiones regulares
            token = [Token(TokenType.LPAREN, self._character)]
        elif match(r'^\)$', self._character): # Se escapa por tener un significado especial en las expresiones regulares
            token = [Token(TokenType.RPAREN, self._character)]
        elif match(r'^,$', self._character):
            token = [Token(TokenType.COMMA, self._character)]
        elif match(r'^;$', self._character):
            token = [Token(TokenType.SEMICOLON, self._character)]
        elif match(r'^<$', self._character):
            token = [Token(TokenType.LT, self._character)]
        elif match(r'^/$', self._character):
            token = [Token(TokenType.DIV, self._character)]
        elif match(r'^-$', self._character):
            token = [Token(TokenType.MINUS, self._character)]
        elif match(r'^\*$', self._character): # Se escapa por tener un significado especial en las expresiones regulares
            token = [Token(TokenType.MULT, self._character)]
        elif match(r'^>$', self._character):
            token = [Token(TokenType.GT, self._character)]
        elif match(r'^!$', self._character):
            if self._peek_character() == '=':
                token = self._make_two_character_token(TokenType.NOT_EQ)
            else: 
                token = [Token(TokenType.EXC, self._character)]
        elif match(r'^:$', self._character):
            token = [Token(TokenType.COLON, self._character)]
        # Funciones auxiliares, en lugar de generar una expresion regular se generan funciones auxiliares
        elif self._is_letter(self._character): # Ahora si nos encontramos frente a un caracter lo que se quiere es generar una literal, donde se genera una funcion y luego se conoce que tipo de Token es
            literal = self._read_identifier()
            # Ahora como podemos tener un identifier o keyword se genera esta funcion
            token_type = lookup_token_type(literal) # Esta funcion se genera en token.py

            return [Token(token_type, literal)] # Se regresa lo que mande la funcion lookup y la literal
        # Se necesita saber si estamos frente a un numero
        elif self._is_number(self._character):
            literal = self._read_number()

            return [Token(TokenType.INT, literal)]
        elif self._is_tab(self._character):
            literal = self._read_tab()
            token = self.indent_algorithm(literal)

            return token # Ya no se necesita regresarlo como lista ya que desde indent algorithm ya viene como lista
        # elif self._is_comment(self._character):
        #     pass
        else:
            token = [Token(TokenType.ILLEGAL, self._character)] 

        """
        Se tiene que escapar especificamente el caracter de suma porque suma significa algo especifico en las expresiones regulares, significa que haga match por lo menos una o mas veces pero aqui no interesa la funcionalidad sino especificamente el caracter, se escapa con la diagonal invertida
        """
        # Escapar: hacer que el caracter sea tomado cómo texto plano en lugar de su significado por defecto en la expreción regular.

        
        # Se necesita correrlo despues de que se genere el token y antes de regresarlo
        self._read_character()
        
        return token # Se regresa el token
    
    
    # Esta funcion permite saber si estamos frente a una letra que podemos reconocer, recibe como parametro el caracter
    def _is_letter(self, character: str) -> bool:
        return bool(match(r'^[a-zA-Z_]$', character)) # Aqui match se convierte en booleano porque vamos a regresar un booleano, se hace un caracter set con las letras que entiende el lenguaje


    def _is_number(self, character: str) -> bool:
        return bool(match(r'^\d$', character)) # Expresion abreviada para encontrar digitos
        

    def _read_number(self) -> str:
        initial_position = self._position  # Se va a leer hasta que se encuentre el final de un numero
        while self._is_number(self._character):
            self._read_character()

        return self._source[initial_position:self._position] 

    def _read_identifier(self) -> str:
        initial_position = self._position

        while self._is_letter(self._character) or self._is_number(self._character): # Se corrije el bug de que no detecte var_1 como identificador
            self._read_character() # Funcion que se implemento en el pasado, avanza un caracter

        return self._source[initial_position:self._position]

    
    def _peek_character(self) -> str: # Funcion para conocer el siguiente caracter que viene y echar un vistazo
        if self._read_position >= len(self._source):
            return ''

        return self._source[self._read_position] # Por eso tenemos position y read position, porque se va viendo la posicion en la cual estamos y la siguiente es la que estamos leyendo constantemente


    def _make_two_character_token(self, token_type: TokenType) -> List[Token]: # Esta funcion toma el caracter actual, avanza y toma el siguiente para fusionarlos
        prefix = self._character # Se toma el prefijo el cual es el caracter actual
        self._read_character() # Nos movemos al siguiente
        suffix = self._character # Lo volvemos a tomar

        return [Token(token_type, f'{prefix}{suffix}')]


    def _read_character(self) -> None:
        if self._read_position >= len(self._source):
            self._character = ''
        else: 
            self._character = self._source[self._read_position]

        self._position = self._read_position
        self._read_position += 1

    
    def _read_tab(self) -> str:
        initial_position = self._position  # Se va a leer hasta que se encuentre el final de toda la identacion
        while self._is_tab(self._character):
            self._read_character()

        return self._source[initial_position:self._position] 


    def _is_tab(self, character: str) -> bool:
        return bool(match(r'^\t$', character))
    

    def _skipSpaces(self) -> None:
        while match(r'^ $', self._character):
            self._read_character()


    def indent_algorithm(self, literal: str) -> List[Token]: # Algoritmo para hacer la revision de si el token es indent or dedent
        dedents = [] # Una lista de tipo Token DEDENT que se regresara para posteriormente hacerle flatting y tener un array de 1 dimension
        flag = False # Bandera que actua como switch para el trigger que desencadena el ultimo token DEDENT
        if len(literal) > self._indents[-1]:
            self._indents.append(len(literal))
            if not flag:
                self._firts_dedent_flag = False
                flag = True
            return [Token(TokenType.INDENT, literal)]
        elif len(literal) < self._indents[-1]:
            while len(literal) < self._indents[-1]:
                self._indents.pop()
                dedents.append(Token(TokenType.DEDENT, literal))
            if not flag:
                self._firts_dedent_flag = False
                flag = True
            return dedents
        elif len(literal) == self._indents[-1]:
            return [Token(TokenType.IGNORE, literal)]