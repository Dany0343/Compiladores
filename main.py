# -*- coding: utf-8 -*-
import math

# Este es un compilador que pasa de un codigo en python a C++

# Variables de archivos
a = open("codigoPythonLineaPorLinea.txt", "w", encoding="utf-8") # Aquí se escribira linea por linea el archivo de entrada
espaciosVacios = 0

def run():
    # Lectura de archivo
    f = open("ProyectoFinal.txt", "r")
    global espaciosVacios # Se especifica que podemos utilizar la variable global

    #Se comienza a iterar el archivo
    for i in f:
        if i != '\n': #Se revisa si el renglon no está vacío
            cadena = i
            # Quitamos identación
            # cadena = cadena.strip()
            a.write(f"{cadena}\n")
        else:
            print("Espacio vacio")
            espaciosVacios += 1

if __name__ == "__main__": # Entry point
    run()