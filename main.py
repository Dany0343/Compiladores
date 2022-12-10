from comp.repl import start_repl
from comp.lecturaArchivo import leer
from comp.ast2 import astGen

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
            leer()
            print("\n\nAhora parseandolo tenemos\n")
            # subprocess.call("sudo source /home/dany0343/dev/Compiladores/venv/bin/activate", shell=True)
            subprocess.call("python3 parser2.py test.py", shell=True)

            print("Se procede a ver el AST")
            filename = 'test.py'
            filename = open(filename, 'r')
            source = ''
            for i in filename: # Extrayendo texto de archivo en un string
                source = source + i

            arbol = astGen(source)
            print(arbol)


        elif opc == 2:
            start_repl()
            os.system('clear')
        elif opc == 3:
            break
        else:
            print("Seleccione una opción valida")


if __name__ == '__main__':
    main()