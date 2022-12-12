#include <iostream>
#include <vector>
#include <numeric>

//function to print message and information
void impresion(std::string mensaje, int informacion)
{
    std::cout << mensaje << " " << informacion << std::endl;
}

//function to fill a vector with user input
std::vector<int> llenarLista(int longitud)
{
    std::vector<int> Contenedor;
    for (int i = 0; i < longitud; i++)
    {
        int elemento;
        std::cout << "Introduce un numero: ";
        std::cin >> elemento;
        Contenedor.push_back(elemento);
    }
    return Contenedor;
}

//function to calculate sum of vector elements
int sumatoria(std::vector<int> Lista)
{
    return std::accumulate(Lista.begin(), Lista.end(), 0);
}

//function to calculate product of vector elements
int calcularProducto(std::vector<int> Lista)
{
    int product = 1;
    for (int i = 0; i < Lista.size(); i++)
    {
        product *= Lista[i];
    }
    return product;
}

int main()
{
    std::cout << "Bienvenido a compiladores" << std::endl;
    int Datos;
    std::cout << "Datos a introducir: ";
    std::cin >> Datos;
    impresion("El usuario introducira", Datos);
    std::vector<int> DatosLista = llenarLista(Datos);
    int Suma = sumatoria(DatosLista);
    impresion("La sumatoria de los numeros es: ", Suma);
    int Producto = calcularProducto(DatosLista);
    impresion("El producto de los numeros es: ", Producto);
    return 0;
}