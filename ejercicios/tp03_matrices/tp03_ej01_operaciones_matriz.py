def _cargar_matriz (n: int) -> list[list[int]]:
    """
    Contrato: Carga una matriz de N x N con números enteros ingresados por el usuario

    Precondicion: n debe ser un entero positivo

    Postcondicion: Devuelve una matriz de tamaño N x N
    
    """

    matriz = []

    fila = 0

    while fila < n:
        fila_actual = []

        columna = 0
        while columna < n:
            valor = int(input("Ingrese un número: "))
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


def _ordenar_filas(matriz: list[list[int]]) -> None:
    """
    Contrato: Ordena de forma ascendente cada fila de la matriz

    Precondicion: matriz debe ser una lista de lista de enteros

    Precondicion: Cada fila de la matriz queda ordenada de forma ascendente
    
    """

    fila = 0
    while fila < len(matriz):
        matriz[fila].sort()
        fila += 1


def _intercambiar_filas(matriz: list[list[int]], fila1: int, fila2: int) -> None:
    """
    Contrato: Intercambia dos filas de la matriz modificando la matriz original
    
    Precondicion: fila1 y fila2 deben ser índices válidos de filas de la matriz

    Postcondicion: Las filas indicadas quedan intercambiadas de posición
    
    """

    fila_temporal = matriz[fila1]
    matriz[fila1] = matriz[fila2]
    matriz[fila2] = fila_temporal

def _intercambiar_columnas(matriz: list[list[int]], columna1: int, columna2: int) -> None:
    """
    Contrato: Intercambia dos columnas de la matriz, modificando la matriz original

    Precondicion: columna1 y columna2 deben ser índices válidos de columnas en la matriz

    Postcondicion: Las columnas quedan intercambiadas de posición
    
    """
    fila = 0
    while fila < len(matriz):
        fila_temporal = matriz[fila][columna1]
        matriz[fila][columna1] = matriz[fila][columna2]
        matriz[fila][columna2] = fila_temporal
        fila += 1


def _transponer_matriz(matriz: list[list[int]]) -> None:
    """
    Contrato: Transpone la matriz sobre ella misma, intercambia elemento[i][j] por elemento[j][i]

    Precondicion: La matriz debe ser cuadrada

    Postcondiciones: La matriz queda modificada transpuesta
    
    """

    fila = 0
    while fila < len(matriz):
        columna = fila +1
        while columna < len(matriz):
            temporal = matriz[fila][columna]
            matriz[fila][columna] = matriz[columna][fila]
            matriz[columna][fila] = temporal
            columna += 1
        fila += 1


def _promedio_fila(matriz: list[list[int]], fila: int) -> float:
    """
    Contrato: Calcula el promedio de los elementos de una fila de la matriz

    Precondicion: fila deber ser un índice válido de fila de la matriz

    Postcondicion: Devuelve el promedio de los elementos de la fila indicada
    
    """

    suma = sum(matriz[fila])
    promedio = suma / len(matriz[fila])

    return promedio


def _porcentaje_impares_columna (matriz: list[list[int]], columna: int) -> float:
    """
    Contrato: Calcula el porcentaje de elementos con valor impar de una columna de la matriz

    Precondicion: columna debe ser un índice válido de columna de la matriz

    Postcondicion: Devuelve el porcentaje de elementos impares de la columna
    
    """
    contador_impares = 0

    fila = 0
    while fila < len(matriz):
        valor = matriz[fila][columna]
        if valor % 2: 
            contador_impares += 1
        fila += 1

    porcentaje = (contador_impares / len(matriz)) * 100

    return porcentaje



def _es_simetrica(matriz: list[list[int]]) -> bool:
    """
    Contrato: Determina si la matriz es simetrica en respecto a su diagonal principal

    Precondiciones: matriz debe ser una matriz cuadrada

    Postcondicion: Devuelve True si la matriz es simetrica, False si no lo es
    
    """

    fila = 0
    while fila < len(matriz):
        columna = fila + 1
        while columna < len(matriz):
            if matriz[fila][columna] != matriz[columna][fila]:
                return False
            columna += 1
        fila += 1

    return True


def _mostrar_menu() -> None:
    """
    Contrato: Muestra las opciones del menú para hacer operaciones sobre la matriz
    
    Precondiciones: -

    Postcondiciones: Muestra el listado de opciones
    
    """

    print("Menú de operaciones")
    print("1. Mostrar la matriz")
    print("2. Ordenar las filas de forma ascendente")
    print("3. Intercambiar dos filas")
    print("4. Intercambiar dos columnas")
    print("5. Transponer la matriz")
    print("6. Calcular el promedio de una fila")
    print("7. Calcular el porcentaje de impares de una columna")
    print("8. Verificar si la matriz es simetrica")
    print("-1 Para salir")



def main () -> None:
    """
    Contrato: Ejecuta el programa principal, carga una matriz y muestra con menú con las operaciones que se pueden hacer

    Precondicion: El archivo debe ejecutarse como programa principal

    Postcondiciones: Ejecuta la operacion elegida hasta que el usuario ingresa -1
    
    """
    print("Operaciones en matrices")

    n = int(input("Ingrese el valor de N: "))
    matriz = _cargar_matriz(n)

    _mostrar_menu()
    opcion = input("Ingrese una opción: ")

    while opcion != "-1":
        if opcion == "1":
            _imprimir_matriz(matriz)

        elif opcion == "2":
            _ordenar_filas(matriz)
            print("filas ordenadas")
            _imprimir_matriz(matriz)

        elif opcion == "3":
            fila1 = int(input("ingrese la primer fila: "))
            fila2 = int(input("Ingrese la segunda fila: "))
            _intercambiar_filas(matriz, fila1, fila2)
            print("Filas intercambiadas")
            _imprimir_matriz(matriz)

        elif opcion == "4":
            columna1 = int(input("Ingrese la primer columna: "))
            columna2 = int(input("Ingrese la segunda columna: "))
            _intercambiar_columnas(matriz, columna1, columna2)
            print("Columnas intercambiadas")
            _imprimir_matriz(matriz)

        elif opcion == "5":
            _transponer_matriz(matriz)
            print("Matriz transpuesta")
            _imprimir_matriz(matriz)

        elif opcion == "6":
            fila = int(input("Ingrese el número de fila: "))
            promedio = _promedio_fila(matriz, fila)
            print(f"Promedio: {promedio}")

        elif opcion == "7":
            columna = int(input("ingrese el número de columna: "))
            porcentaje = _porcentaje_impares_columna(matriz, columna)
            print(f"Porcentaje: {porcentaje}")

        elif opcion == "8":
            simetrica = _es_simetrica(matriz)
            _imprimir_matriz(matriz)
            print(f"La matriz es simetrica? {simetrica}")

        else:
            print("Opción invalida")

        _mostrar_menu()
        opcion= input("ingrese una opción: ")

    print("Saliendo")
    

main()