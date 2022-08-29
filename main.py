# -*- coding: utf-8 -*-
import math
import re
import keyword

# Este es un compilador que pasa de un codigo en python a C++

# Variables de archivos
a = open("codigoPythonLineaPorLinea.txt", "w", encoding="utf-8") # Aquí se escribira linea por linea el archivo de entrada
espaciosVacios = 0
palabrasReservadasCpp = [ "auto", "const", "double", "float", "int", "short", "struct", "unsigned", "break", "continue", "else", "for", "long", "signed", "switch", "void", "case", "default", "enum", "goto", "register", "sizeof", "typedef", "volatile", "char", "do", "extern", "if", "return", "static", "union", "while", "asm", "dynamic_cast", "namespace", "reinterpret_cast", "try", "bool", "explicit", "new", "static_cast", "typeid", "catch", "false", "operator", "template", "typename", "class", "friend", "private", "this", "using", "const_cast", "inline", "public", "throw", "virtual", "delete", "mutable", "protected", "true", "wchar_t", "and", "bitand", "compl", "not_eq", "or_eq", "xor_eq", "and_eq", "bitor", "not", "or", "xor" 
]
palabrasReservadasPython = keyword.kwlist

def run():
    # Lectura de archivo
    f = open("ProyectoFinal.txt", "r")
    global espaciosVacios # Se especifica que podemos utilizar la variable global

    #Se comienza a iterar el archivo
    for i in f:
        if i != '\n': #Se revisa si el renglon no está vacío
            cadena = i # Equivale al renglon actual del archivo
            # Quitar identación
            # cadena = cadena.strip()
            a.write(f"{cadena}\n")

            # Revisar si caracteres especiales están completos
        else:
            espaciosVacios += 1
            print(f"Espcacios vacios encontrados: {espaciosVacios}")
            

if __name__ == "__main__": # Entry point
    run() 