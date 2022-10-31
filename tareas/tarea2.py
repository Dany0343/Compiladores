"""
Realizar un programa que permita al usuario introducir caracteres hasta que se reciba alguno que usted defina como límite. La cadena conformada deberá ser evaluada mediante una expresión regular para determinar si tiene o no el formato requerido para ser considerado como CURP.
"""

def main():
	caracteres = []
	CURP = ''
	while True:
		char = input("Introduce caracteres, para terminar ingresa '@': \n")
		if char == '@':
			print("Hasta pronto!")
			break
		else: 
			caracteres.append(char)

	for i in caracteres:
		CURP = CURP + i
	
	print(f'La cadena final es: {CURP}')

if __name__ == '__main__':
	main()