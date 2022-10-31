import re
"""
Realizar un programa que permita al usuario introducir caracteres hasta que se reciba alguno que usted defina como límite. La cadena conformada deberá ser evaluada mediante una expresión regular para determinar si tiene o no el formato requerido para ser considerado como CURP.
"""

def main():
	caracteres = []
	CURP = ''
	while True:
		char = input("Introduce caracteres, para terminar ingresa '@': \n")
		if char == '@':
			print("Hasta pronto!\n")
			break
		else: 
			caracteres.append(char)

	for i in caracteres:
		CURP = CURP + i

	print(f'La cadena final es: {CURP}, su longitud es: {len(CURP)}')

	if validacion(CURP):
		print("La cadena tiene el formato requerido")
	else:
		print("La cadena NO tiene el formato requerido")


def validacion(CURP): #BUBO010903HNECRSA5
	x = re.search("^[A-Z][AEIOU][A-Z][A-Z][0-9][0-9][0-9][0-9][0-9][0-9][HM][A-Z][A-Z][BCDFGHJKLMNPQRSTVWXYS][BCDFGHJKLMNPQRSTVWXYS][BCDFGHJKLMNPQRSTVWXYS][0-9A-Z][0-9]$", CURP)
	
	if x:
		return True
	else:
		return False


if __name__ == '__main__':
	main()