def _sumar_cadenas(cadena1: str, cadena2: str) -> float:
    """
    Contrato: Suma dos números reales recibivos como strings y devuelve el resultado como número real

    Precondición: cadena1 y cadena2 deber ser strings

    Postcondición: Devuelve la suma de los valores como número real o -1 si alguna de los strings no es válido
    """
    try:
        numero1 = float(cadena1)
        numero2 = float(cadena2)
        resultado = numero1 + numero2
    except ValueError:
        resultado = -1

    return resultado


def main() -> None:
    """
    Contrato: Ejecuta el programa principal, pide dos strings hasta que el primer string sea vacio e intenta sumarlos

    Precondición: El archivo debe ejecutarse como programa principal

    Postcondición: Muestra el resultado de cada suma
    """
    print("Suma de números ingresados como strings")

    cadena1 = input("Ingrese el primer número (vacío para terminar): ")

    while cadena1 != "":
        cadena2 = input("Ingrese el segundo número: ")

        resultado = _sumar_cadenas(cadena1, cadena2)
        print(f"Resultado: {resultado}")

        cadena1 = input("Ingrese el primer número (vacío para terminar): ")


main()
