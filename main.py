from comp.repl import start_repl
from comp.lecturaArchivo import leer

def main() -> None:
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
    while True:
        opc = input("Opciones\n1. Leer el programa automaticamente desde un archivo\n2. Introducir el código a ser compilado\n3. Salir\n>> ")
        if opc == '1':
            pass
        elif opc == '2':
            start_repl()
        elif opc == '3':
            break
        else:
            print("Seleccione una opción valida")


if __name__ == '__main__':
    main()