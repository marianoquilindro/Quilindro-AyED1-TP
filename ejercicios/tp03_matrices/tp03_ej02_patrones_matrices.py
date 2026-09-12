def _generar_matriz_a(n: int) -> list[list[int]]:
    """
    Contrato: Genera una matriz de N x N poniendo los números impares en la diagonal descendente de izquierda a derecha y ceros en las demás posiciones

    Precondicion: n debe ser un entero positivo

    Postcondicion: Devuelve la matriz con el patrón

    """
    matriz = []

    fila = 0
    while fila < n:
        fila_actual = []

        columna = 0
        while columna < n:
            if fila == columna:
                valor = fila * 2 + 1
            else:
                valor = 0

            fila_actual.append(valor)
            columna += 1

        matriz.append(fila_actual)
        fila += 1

    return matriz


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


def main() -> None:
    """
    Contrato: Ejecuta el programa principal, solicita un número n y genera la matriz con el patrón indicado

    Precondicion: El archivo debe ejecutarse como programa principal

    Postcondicion: Muestra la matriz generada
    
    """

    print("Generación de la matriz del punto a")

    n = int(input("Ingrese el valor de n: "))

    matriz = _generar_matriz_a(n)

    print("Matriz generada")
    _imprimir_matriz(matriz)

main()