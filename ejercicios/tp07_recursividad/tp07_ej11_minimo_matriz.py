import random as rn


def _minimo_fila(fila: list) -> int:
    """
    Contrato: Busca el elemento mas chico de una fila de la matriz de manera recursiva

    Precondición: fila debe ser una lista de números con al menos un elemento

    Postcondición: Devuelve el elemento mas chico de la fila
    """
    if len(fila) == 1:
        minimo = fila[0]
    else:
        minimo_resto = _minimo_fila(fila[1:])

        if fila[0] < minimo_resto:
            minimo = fila[0]
        else:
            minimo = minimo_resto

    return minimo


def _minimo_matriz(matriz: list) -> int:
    """
    Contrato: Busca el elemento mas chico de una matriz de manera recursiva

    Precondición: matriz debe ser una lista de lista de números con al menos una fila y una columna

    Postcondición: Devuelve el elemento mas chico de la matriz
    """
    if len(matriz) == 1:
        minimo = _minimo_fila(matriz[0])
    else:
        minimo_primera = _minimo_fila(matriz[0])
        minimo_resto = _minimo_matriz(matriz[1:])

        if minimo_primera < minimo_resto:
            minimo = minimo_primera
        else:
            minimo = minimo_resto

    return minimo


def _formatear_fila(fila: list) -> str:
    """
    Contrato: Convierte una fila de la martiz en una cadena de manera recursiva

    Precondición: fila debe ser una lista de números

    Postcondición: Devuelve la cadena con todos los elementos de la fila en columnas
    """
    if len(fila) == 0:
        texto = ""
    else:
        texto = (f"{fila[0]:>6}") + _formatear_fila(fila[1:])

    return texto


def _imprimir_matriz(matriz: list) -> None:
    """
    Contrato: Imprime una matriz de manera recursiva

    Precondición: matriz debe ser una lista de lista de números, donde todas tengan la misma longitud

    Postcondición: Muestra la matriz
    """
    if len(matriz) > 0:
        print(_formatear_fila(matriz[0]))
        _imprimir_matriz(matriz[1:])


def _crear_matriz(filas: int, columnas: int) -> list:
    """
    Contrato: Crea una matriz de filas x columnas con números enteros aleatorios

    Precondición: filas y columnas deben ser números enteros mayores o iguale a 1

    Postcondición: Devuelve la matriz
    """
    matriz = []

    for i in range(filas):
        fila = []

        for j in range(columnas):
            fila.append(rn.randint(0, 99))

        matriz.append(fila)

    return matriz


def _ingresar_dimensiones() -> int:
    """
    Contrato: Pide la dimensión de la matriz hasta que sea un número válido

    Precondición: -

    Postcondición: Devuelve la dimensión ingresada
    """
    dimension = 0

    while dimension < 1:
        try:
            dimension = int(input("Ingrese la dimensión de la matriz: ").strip())

            if dimension < 1:
                print("Debe ser un número mayor o igual a 1")
        except ValueError:
            print("Debe ingresar un número entero")

    return dimension


def main() -> None:
    """
    Contrato: Ejecuta el programa principal, pide las dimensiones de una matriz y la crea con números aleatorios

    Precondición: El archivo debe ejecutarse como programa principal

    Postcondición: Muestra la matriz y su elemento más chico
    """
    print("Elemento mas chico de una matriz")

    print("Cantidad de filas")
    filas = _ingresar_dimensiones()

    print("Cantidad de columnas")
    columnas = _ingresar_dimensiones()

    matriz = _crear_matriz(filas, columnas)

    print(f"Matriz de {filas} x {columnas}")
    _imprimir_matriz(matriz)

    print(f"Elemento más chico de la matriz: {_minimo_matriz(matriz)}")


main()
