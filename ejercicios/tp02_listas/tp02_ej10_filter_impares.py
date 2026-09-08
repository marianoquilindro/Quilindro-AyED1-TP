import random as rn

def _generar_lista (cantidad: int) -> list:
    """
    Contrato: Genera una lista de numeros al azar entre 1 y 100
    
    Precondicion: cantidad debe ser un entero positivo

    Postcondicion: Devuelve una lista de enteros entre 1 y 100

    """
    lista = []

    for i in range(cantidad):
        lista.append(rn.randint(1,100))

    return lista


def _impar (numero: int) -> bool:
    """
    Contrato: Determina si un numero es impar

    Precondicion: numero debe ser un entero
    
    Postcondicion: Devuelve True si el numero es impar, Falso si no lo es

    """

    return numero % 2 != 0





def main() -> None:
    """
    Contrato: Ejecuta el programa principal, solicita una cantidad, genera una lista al azar con esa cantidad y obtiene sus elementos impares

    Precondicion: El archivo debe ejecutarse como programa principal

    Postcondicion: Muestra ambas listas 
    
    """

    cantidad = int(input("ingrese la cantidad de numeros a generar: "))

    lista = _generar_lista(cantidad)

    impares = list(filter(_impar,lista))

    print(f"Lista original: {lista}")
    print(f"Lista de impares: {impares}")

main()


