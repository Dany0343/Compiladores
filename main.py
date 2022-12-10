from comp.repl import start_repl
from comp.lecturaArchivo import leer
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

        elif opc == 2:
            start_repl()
            os.system('clear')
        elif opc == 3:
            break
        else:
            print("Seleccione una opción valida")


if __name__ == '__main__':
    main()