// -Codigo:-
#include <iostream>
#include <string>
using namespace std;

void impresion(string mensaje,int informacion){
	cout<<mensaje<<informacion<<endl;
}
int* llenarLista(int longitud){
	int* Contenedor=new int[longitud];
	for (int i = 0; i < longitud; ++i)
	{
		int elemento;
		cout<<"Introduce un numero: ";
		cin>>elemento;
		Contenedor[i]=elemento;
	}
	return Contenedor;
}
int sumatoria(int* Lista,int longitud){
	int suma=0;
	for (int i = 0; i < longitud; ++i)
	{
		suma=suma+Lista[i];
	}
	return suma;
}
int calcularProducto(int* Lista,int longitud){
	int vActual=Lista[0];
	for (int i = 1; i < longitud; ++i)
	{
		vActual=Lista[i]*vActual;
	}
	return vActual;
}

int main(){
	cout<<"Bienvenido a compiladores"<<endl;
	int Datos;
	cout<<"Datos a introducir: ";
	cin>>Datos;
	impresion("El usuario introducira",Datos);
	int* Datos2=llenarLista(Datos);
	int Suma=sumatoria(Datos2,Datos);
	impresion("La sumatoria de los numeros es: ",Suma);
	int Producto=calcularProducto(Datos2,Datos);
	impresion("El producto de los numeros es: ",Producto);
	return 0;
}

