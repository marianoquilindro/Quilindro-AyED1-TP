def _cantidad_digitos(numero: int) -> int:
    """
    Contrato: Calcula la cantidad de digitos de un número entero de manera recursiva

    Precondición: numero debe ser un número entero

    Postcondición: Devuelve la cantidad de dígitos del número
    """
    if numero < 0:
        cantidad = _cantidad_digitos(-numero)
    elif numero < 10:
        cantidad = 1
    else:
        cantidad = 1 + _cantidad_digitos(numero // 10)

    return cantidad


def _ingresar_entero() -> int:
    """
    Contrato: Pide un número entero hasta que se ingresa uno válido

    Precondición: -

    Postcondición: Devuelve el número entero ingresado
    """
    numero = None

    while numero is None:
        try:
            numero = int(input("Ingrese un número entero: ").strip())
        except ValueError:
            print("Debe ingresar un número entero")

    return numero


def main() -> None:
    """
    Contrato: Ejecuta el programa principal, pide un número y muestra cuántos dígitos tiene

    Precondición: El archivo debe ejecutarse como programa principal

    Postcondición: Muestra la cantidad de dígitos del numero ingresado
    """
    print("Cantidad de dígitos de un número entero")

    numero = _ingresar_entero()

    print(f"El número {numero} tiene {_cantidad_digitos(numero)} dígitos")


main()
