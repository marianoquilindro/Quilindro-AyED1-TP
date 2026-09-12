import random as rn

def _imprimir_matriz(matriz: list[list[int]]) -> None:
    """
    Contrato: Imprime la matriz, mostrando cada fila en una linea distinta
    
    Precondicion: matriz debe ser una lista de lista de enteros

    Postcondicion: Muestra el contenido de la matriz
    
    """

    fila = 0
    while fila < len(matriz):
        print(matriz[fila])
        fila += 1


def _generar_matriz_sin_repetidos(n: int) -> list[list[int]]:
    """
    Contrato: Genera una matriz de N x N con números al azar entre 0 y N al cuadrado -1 sin ningun numero repetido

    Precondicion: n debe ser un entero positivo

    Postcondicion: Devuelva una matriz de N x N con números sin repetir entre 0 y N al cuadrado -1
    
    """

    limite = (n ** 2) -1

    num_usados = []
    matriz = []

    fila = 0
    while fila < n:
        fila_actual = []
        columna = 0

        while columna < n:
            valor = rn.randint(0, limite)

            while valor in num_usados:
                valor = rn.randint(0, limite)

            num_usados.append(valor)
            fila_actual.append(valor)
            columna += 1

        matriz.append(fila_actual)
        fila += 1

    return matriz


def main() -> None:
    """
    Contrato: Ejecuta el programa principal solicita un número N y genera una matriz con numeros al azar sin repetirse

    Precondicion: El archivo debe ejecutarse como programa principal

    Postcondicion: Muestra la matriz generada
    
    """

    n = int(input("ingrese el valor de N: "))

    matriz = _generar_matriz_sin_repetidos(n)

    _imprimir_matriz(matriz)


main()