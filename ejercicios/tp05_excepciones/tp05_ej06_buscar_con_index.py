def _cargar_lista() -> list:
    """
    Contrato: Carga una lista con números enteros ingresados por teclado, finalizando la carga cuando el usuario ingresa -1

    Precondición: El usuario debe ingresar números enteros

    Postcondición: Devuelve la lista con los números enteros ingresados
    """

    lista = []

    entrada = input("Ingrese un número entero (-1 para terminar): ")

    while entrada != "-1":
        try:
            lista.append(int(entrada))
        except ValueError:
            print("Debe ingresar un número entero")

        entrada = input("Ingrese un número entero (-1 para terminar): ")

    return lista


def _buscar_posicion(lista: list, valor: int) -> int:
    """
    Contrato: Busca un valor dentro de una lista usando index

    Precondición: lista debe ser una lista de números enteros y valor un número entero

    Precondición: Devuelve la posición del valor dentro de la lista o -1 si el valor no esta en la lista
    """
    try:
        posicion = lista.index(valor)
    except ValueError:
        posicion = -1

    return posicion


def main() -> None:
    """
    Contrato: Ejecuta el programa principal, carga una lista de enteros y permite buscar la posición de distintos valores

    Precondición: El archivo debe ejecutarse como programa principal

    Postcondición: Muestra la posición de cada valor encontrado o mensaje de error si el valor no pertenece a la lista
    """

    print("Búsqueda por posiciones en una lista")

    lista = _cargar_lista()
    errores = 0

    entrada = input("Ingrese un número a buscar (vacío para terminar): ")

    while entrada != "" and errores < 3:
        try:
            valor = int(entrada)
            posicion = _buscar_posicion(lista, valor)

            if posicion == -1:
                errores += 1
                print(f"El número no pertenece a la lista. Errores: {errores}")
            else:
                print(f"El número se encuentra en la posición: {posicion + 1}")
        except ValueError:
            print("Debe ingresar un número entero")

        if errores < 3:
            entrada = input("Ingrese un número a buscar (vacío para terminar): ")

        if errores == 3:
            print("3 errores, saliendo...")


main()
