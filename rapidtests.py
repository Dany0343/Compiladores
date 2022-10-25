import tokenize
import io
p = '''\
def impresion(mensaje,informacion):#8udugduwu
	print(mensaje,informacion)
def llenarLista(longitud):
	Contenedor=[]
	for i in range(0, longitud):
		elemento = int(input("Introduce un numero: "))
		Contenedor.append(elemento) 
	return Contenedor
def sumatoria(Lista):
	suma=0
	for x in range ,len(Lista)):
		suma=suma+Lista[x]
	return suma
def calcularProducto(Lista):
	vActual=Lista[0]
	for x in range(1,len(Lista)):
		vActual=Li sta[x]*vActual
	return vActual

print("Bienvenido a compiladores")
Datos=input("Datos a introducir: ")
impresion("El usuario introducira",Datos)
Datos=llenarLista(int(Datos))
Suma=sumatoria(Datos)
impresion("La sumatoria de los numeros es: ",Suma)
Producto=calcularProducto(Datos)
impresion("El producto de los numeros es: ",Producto)
'''
text = tokenize.generate_tokens(io.StringIO(p).readline)
[print(tok) for tok in text]
	

'''
a
	e
	e
	e	d
		e
			f
				g
					h
					i
						j
					k
				l
			m
		n
		o
	o
sup
'''