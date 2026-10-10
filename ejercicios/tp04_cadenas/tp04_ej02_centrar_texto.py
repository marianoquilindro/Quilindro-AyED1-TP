def _centrar_cadena(cadena: str) -> str:
    """
    Contrato: Agrega espacios en un string para que quede centrado en una pantalla de 80 columnas

    Precondición: cadena debe ser un str de 80 caracteres como maximo

    Postcondición: Devuelve el string centrado

    """

    columnas = 80
    espacios = (columnas - len(cadena)) // 2

    cadena_centrada = " " * espacios + cadena

    return cadena_centrada


def main() -> None:
    """
    Contrato: Ejecuta el programa principal, verifica el comportamiento de la función

    Precondición: El archivo debe ejecutarse como programa principal

    Postcondición: Muestra el resultado de la implementación de la función

    """

    print("Cadena centrada")

    cadena = input("Ingrese una cadena de caracteres: ")

    print("-" * 80)
    print(_centrar_cadena(cadena))
    print("-" * 80)


main()
