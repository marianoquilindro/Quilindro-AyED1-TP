def _es_capicua(cadena: str) -> bool:
    """
    Contrato: Determina si una cadena es capicúa, comparando los elementos desde los extremos hasta el medio

    Precondición: cadena debe ser un string

    Postcondición: Devuelve True si la cadena es capicúa, False si no lo es

    """

    izquierda = 0
    derecha = len(cadena) - 1

    while izquierda < derecha:
        if cadena[izquierda] != cadena[derecha]:
            return False
        izquierda += 1
        derecha -= 1

    return True


def main() -> None:
    """
    Contrato: Ejecuta el programa principal, verifica el comportamiento de la función

    Precondición: El archivo debe ejecutarse como programa principal

    Postcondición: Muestra los resultados de la implementación de la función

    """

    print("Verificacion de capicúas")

    cadena = input("Ingrese cadena de caracteres: ")
    print(f"{cadena} es capicua? {_es_capicua(cadena)}")


main()
