def _producto(a: int, b: int) -> int:
    """
    Contrato: Calcula el producto de dos números enteros mediante sumas sucesivas de manera recursiva

    Precondición: a y b deben ser números enteros

    Postcondición: Devuelve el producto de a por b
    """
    if b == 0:
        producto = 0
    elif b > 0:
        producto = a + _producto(a, b - 1)
    else:
        producto = -_producto(a, -b)

    return producto


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
    Contrato: Ejecuta el programa principal, pide dos números enteros y muestra su producto

    Precondición: El archivo debe ejecutarse como programa principal

    Postcondición: Muestra el producto de los números o un mensaje si los números son muy grandes para resolverlo por recursión
    """
    print("Producto de dos números usando recursión")

    a = _ingresar_entero()
    b = _ingresar_entero()

    try:
        print(f"{a} x {b} = {_producto(a, b)}")
    except RecursionError:
        print("Los números son muy grandes para resolverlo con recursión")


main()
