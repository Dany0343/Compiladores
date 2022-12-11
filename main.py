from comp.repl import start_repl
from comp.lecturaArchivo import leer
from comp.ast2 import (
    astGen,
    jsonAst
)
from comp.openai import run
import os
import subprocess

def main() -> None:
    while 1:
        print('''

     /$$$$$$$  /$$                                                   /$$       /$$          
    | $$__  $$|__/                                                  |__/      | $$          
    | $$  \ $$ /$$  /$$$$$$  /$$$$$$$  /$$    /$$ /$$$$$$  /$$$$$$$  /$$  /$$$$$$$  /$$$$$$ 
    | $$$$$$$ | $$ /$$__  $$| $$__  $$|  $$  /$$//$$__  $$| $$__  $$| $$ /$$__  $$ /$$__  $$
    | $$__  $$| $$| $$$$$$$$| $$  \ $$ \  $$/$$/| $$$$$$$$| $$  \ $$| $$| $$  | $$| $$  \ $$
    | $$  \ $$| $$| $$_____/| $$  | $$  \  $$$/ | $$_____/| $$  | $$| $$| $$  | $$| $$  | $$
    | $$$$$$$/| $$|  $$$$$$$| $$  | $$   \  $/  |  $$$$$$$| $$  | $$| $$|  $$$$$$$|  $$$$$$/
    |_______/ |__/ \_______/|__/  |__/    \_/    \_______/|__/  |__/|__/ \_______/ \______/ 
                                                                                        
                                                                                        
    ''')
        print("Bienvenido al compilador de Python a C++")
        opc = int(input("Opciones\n1. Leer el programa automaticamente desde un archivo\n2. Introducir el código a ser compilado\n3. Salir\n>> "))
        if opc == 1:
            os.system('clear')
            leer()
            input("\n\nPresiona enter para continuar...")
            os.system('clear')

            os.system('clear')
            print("\n\nAhora parseandolo tenemos\n")
            # subprocess.call("sudo source /home/dany0343/dev/Compiladores/venv/bin/activate", shell=True)
            try:
                subprocess.call("python3 parser2.py ProyectoFinal.txt", shell=True)
                print("\n\nSe procede a ver el AST\n")
                filename = 'ProyectoFinal.txt'
                filename = open(filename, 'r')
                source = ''
                for i in filename: # Extrayendo texto de archivo en un string
                    source = source + i

                astGen(source)
                input("\n\nPresiona enter para continuar...")
                os.system('clear')

                os.system('clear')
                print("\nUna opción que se vea mejor\n")
                jsonAst(source)
                input("\n\nPresiona enter para continuar...")
                os.system('clear')

                os.system('clear')
                print("Se procede a transformar el AST")
                print("Compilando...")
                run()


            except SyntaxError:
                print("El codigo tiene errores, revise de nuevo")



        elif opc == 2:
            start_repl()
            os.system('clear')
        elif opc == 3:
            break
        else:
            print("Seleccione una opción valida")


if __name__ == '__main__':
    main()