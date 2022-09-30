from comp.lexer import Lexer
from comp.token import(
    Token,
    TokenType
)

EOF_TOKEN: Token = Token(TokenType.EOF, '') # Variable global que nos indica el fin del programa

def main():
    filename = 'ProyectoFinal.txt'
    file = open(filename, 'r')
    lexer: Lexer = Lexer(filename)

    while(token := lexer.next_token()) != EOF_TOKEN:
        print(token)

main()