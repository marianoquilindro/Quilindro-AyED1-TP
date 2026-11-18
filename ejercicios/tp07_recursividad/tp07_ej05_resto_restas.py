def _resto(dividendo: int, divisor: int) -> int:
    """
    Contrato: Calcula el resto de dividir dos números enteros de manera recursiva

    Precondición: dividendo debe ser un número entero y divisor un número entero distinto a 0

    Postcondición: Devuelve el resto de dividir el dividendo por el divisor
    """
    if divisor < 0:
        resto = _resto(dividendo, -divisor)
    elif dividendo < 0:
        resto = -_resto(-dividendo, divisor)
    elif dividendo < divisor:
        resto = dividendo
    else:
        resto = _resto(dividendo - divisor, divisor)

    return resto


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
    Contrato: Ejecuta el programa principal, pide dos números enteros y muestra el resto de dividir el primero por el segundo

    Precondición: El archivo debe ejecutarse como programa principal

    Postcondición: Muestra el resto de la división o un aviso si los números son muy grandes para resolverlo con recursión
    """
    print("Resto de dos números enteros usando recursión")

    dividendo = _ingresar_entero()
    divisor = _ingresar_entero()

    while divisor == 0:
        print("El divisiron no puede ser 0")
        divisor = _ingresar_entero()

    try:
        print(
            f"El resto de {dividendo} dividido {divisor} es {_resto(dividendo,divisor)}"
        )
    except RecursionError:
        print("Los números son demasiado grandes para resolverlo con recursión")


main()
