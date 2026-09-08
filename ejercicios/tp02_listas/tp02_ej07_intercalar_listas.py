def _intercalar(lista1: list, lista2: list) -> None:
    """
    Contrato: Intercala los elementos de la lista2 entre los elementos de la lista1

    Precondicion: lista1 y lista2 deben contener enteros

    Postcondicion: lista1 queda modificada con los elementos de lista2 intercalados
    
    """

    for indice, valor in enumerate(lista2):
        posicion = 2 * indice + 1
        lista1[posicion:posicion] = [valor]


def main() -> None:
    """
    Contrato: Ejecuta el programa principal, verifica el comportamiento de la funcion

    Precondicion: El archivo debe ejecutarse como programa principal

    Postcondicion: Muestra el resultado de las pruebas
    
    """

    print("Pruebas")

    lista1 = [1,3,5,7,9]
    lista2 = [2,4,6,8,0]

    print(f"Lista 1: {lista1}")
    print(f"Lista 2: {lista2}")

    _intercalar(lista1,lista2)

    print(f"Lista 1 modificada: {lista1}")

main()