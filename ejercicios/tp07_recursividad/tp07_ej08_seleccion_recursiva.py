def _indice_del_minimo(lista: list) -> int:
    """
    Contrato: Busca la posición del elemento mas chico de una lista, comparando elemento por elemento

    Precondición: lista debe tener al menos un elemento

    Postcondición: Devuelve la posición del elemento mas chico
    """
    indice = 0

    for posicion in range(1, len(lista)):
        if lista[posicion] < lista[indice]:
            indice = posicion

    return indice


def _ordenar_por_seleccion(lista: list) -> list:
    """
    Contrato: Ordena una lista de menor a mayor de manera recursiva

    Precondición: lista debe ser una lista de enteros

    Postcondición: Devuelve una lista nueva con los elementos ordenados de menor a mayor
    """
    if len(lista) <= 1:
        ordenada = lista[:]
    else:
        indice = _indice_del_minimo(lista)
        minimo = lista[indice]
        resto = lista[:indice] + lista[indice + 1 :]
        ordenada = [minimo] + _ordenar_por_seleccion(resto)

    return ordenada


def _ingresar_lista() -> list:
    """
    Contrato: Pide números enteros y los agrega a una lista hasta que se ingresa una cadena vacía

    Precondición: -

    Postcondición: Devuelve una lista con los números enteros ingresados
    """
    numeros = []

    entrada = input("Ingrese un número entero (vacío para terminar): ").strip()

    while entrada != "":
        try:
            numeros.append(int(entrada))
        except ValueError:
            print("Debe ingresar un número entero")
        entrada = input("Ingrese un número entero (vacío para terminar): ").strip()

    return numeros


def main() -> None:
    """
    Contrato: Ejecuta el programa principal, lee una lista de números y la muestra ordenada de menor a mayor

    Precondición: El archivo debe ejecutarse como programa principal

    Postcondición: Muestra la lista original y la lista ordenada, o mensaje si la lista es muy larga para ordenarla por recursión
    """
    print("Ordenamiento por selección")

    lista = _ingresar_lista()

    if len(lista) == 0:
        print("No se ingresaron números")
    else:
        try:
            ordenada = _ordenar_por_seleccion(lista)

            print(f"Lista original: {lista}")
            print(f"Lista ordenada: {ordenada}")
        except RecursionError:
            print("La lista es muy larga para ordenarla por recursión")


main()
