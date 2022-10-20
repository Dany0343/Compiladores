def leer():
    # filename = 'ProyectoFinal.txt'
    filename = 'ProyectoFinal.txt'
    filename = open(filename, 'r')
    
    print("\n\n")

    print("Código Final: \n")
    for i in filename:
        for j in i:
            print(f"{j}")

leer()