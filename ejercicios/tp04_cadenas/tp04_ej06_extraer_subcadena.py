def _extraer_con_slices(cadena: str, posicion: int, cantidad: int) -> str:
    """
    Contrato: Saca una subcadena de una cadena, indicando la posición de inicio y la cantidad de caracteres usando slices

    Precondición: cadena debe ser una cadena de strings, posición un entero mayor o igual a 0 y cantidad un entero positivo

    Postcondición: Devuelve la subcadena obtenida o los caracteres disponibles si piden mas de los que quedan
    """
    return cadena[posicion : posicion + cantidad]


def _extraer_sin_slices(cadena: str, posicion: int, cantidad: int) -> str:
    """
    Contrato: Saca una subcadena de una cadena, indicado la posición de inicio y la cantidad de caracteres sin usar slices

    Precondición: cadena debe ser una cadena de strings, posición un entero mayor o igual a 0 y cantidad un entero positivo

    Postcondición: Devuelve la subcadena obtenida o los caracteres disponibles si piden mas de los que quedan
    """

    subcadena = ""

    indice = posicion
    while indice < posicion + cantidad and indice < len(cadena):
        subcadena += cadena[indice]
        indice += 1

    return subcadena


def main() -> None:
    """
    Contrato: Ejecuta el programa principal, solicita una cadena, una posición y una cantidad y muestra la subcadena obtenida con las distintas funciones

    Precondición: El archivo debe ejecutarse como programa principal

    Postcondición: Muestra el resultado de cada función
    """

    print("Extracción de subcadenas")

    cadena = input("Imgrese una cadena de texto: ")
    posicion = int(input("Ingrese la posicion de inicio: "))
    cantidad = int(input("Ingrese la cantidad de caracteres: "))

    print(f"1) Con slices: {_extraer_con_slices(cadena,posicion,cantidad)}")
    print(f"2) Sin slices: {_extraer_sin_slices(cadena,posicion,cantidad)}")


main()
