def _eliminar_con_slices(cadena: str, posicion: int, cantidad: int) -> str:
    """
    Contrato: Elimina una subcadena de una cadena a partir de una posicion y una cantidad de caracteres usando slices

    Precondición: cadena debe ser un string, posicion un entero mayor o igual a 0 y cantidad un entero positivo

    Postcondición: Devuelve la cadena resultante
    """

    return cadena[:posicion] + cadena[posicion + cantidad :]


def _eliminar_sin_slices(cadena: str, posicion: int, cantidad: int) -> str:
    """
    Contrato: Elimina una subcadena de una cadena a partir de una posicion y una cantidad de caracteres sin usar slices

    Precondición: cadena debe ser un string, posicion un entero mayor o igual a 0 y cantidad un entero positivo

    Postcondición: Devuelve la cadena resultante
    """

    resultado = ""

    indice = 0
    while indice < len(cadena):
        if indice < posicion or indice >= posicion + cantidad:
            resultado += cadena[indice]
        indice += 1

    return resultado


def main() -> None:
    """
    Contrato: Ejecuta el programa principal, solicita un string, una posicion y una cantidad, luego muestra la cadena resultante de ambas funciones

    Precondición: El archivo debe ejecutarse como programa principal

    Postcondición: Muestra el resultado de cada función
    """

    print("Eliminación de subcadenas")

    cadena = input("Ingrese una cadena de caracteres: ")
    posicion = int(input("Ingrese la posición de inicio: "))
    cantidad = int(input("Ingrese la cantidad de caracteres a eliminar: "))

    print(f"1) con slices: {_eliminar_con_slices(cadena,posicion,cantidad)}")
    print(f"2) sin slices: {_eliminar_sin_slices(cadena,posicion,cantidad)}")


main()
