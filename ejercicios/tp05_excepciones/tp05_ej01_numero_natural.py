def _convertir_a_natural(cadena: str) -> int:
    """
    Contrato: Convierte una cadena a un número natural, controlando que sea un número entero y mayor a 0

    Precondición: cadena debe ser un string

    Postcondición: Devuelve el número natural como entero o lanza ValueError con un mensaje de la razón del error
    """
    try:
        numero = float(cadena)
    except ValueError:
        raise ValueError("el texto ingresado no es un número")

    if numero % 1 != 0:
        raise ValueError("el número no es entero")

    if numero <= 0:
        raise ValueError("el numero debe ser mayor a 0")

    return int(numero)


def _ingresar_natural() -> int:
    """
    Contrato: Solicita y verifica que lo ingresado sea un número natural, repite el pedido hasta que pase la verificación

    Precondición: -

    Postcondición: Devuelve el número natural entero y mayor a 0 ingresado
    """
    while True:
        numero = input("Ingrese un número natural: ")

        try:
            return _convertir_a_natural(numero)
        except ValueError as error:
            print(f"Error: {error}")


def main() -> None:
    """
    Contrato: Ejecuta el programa principal, solicita un número natural y muestra la conversión

    Precondición: El archivo debe ejecutarse como programa pricipal

    Postcondición: Muestra el número ingresado
    """

    print("Ingreso de un número natural")

    numero = _ingresar_natural()
    print(f"Ingreso correctamente el número {numero}")

    casos_prueba = ["7", "abc", "3.5", "0", "-4", ""]

    for caso in casos_prueba:
        try:
            resultado = _convertir_a_natural(caso)
            print(f"'{caso} -> válido: {resultado}")
        except ValueError as error:
            print(f"'{caso} -> rechazado: {error}")


main()
