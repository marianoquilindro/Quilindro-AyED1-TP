def _suma_naturales(n: int) -> int:
    """
    Contrato: Calcula la suma de los N primeros njmeros naturales de manera recursiva

    Precondición: n debe ser un número entero mayor o igual a 0

    Postcondición: Devuelve la suma de los primeros n números naturales
    """
    if n == 0:
        suma = 0
    else:
        suma = n + _suma_naturales(n - 1)

    return suma


def _ingresar_n() -> int:
    """
    Contrato: Pide la cantidad N de números naturales hasta que sea un número entero mayor o igual a 0

    Precondición: -

    Postcondición: Devuelve el número n ingresado
    """
    n = None

    while n is None:
        try:
            candidato = int(input("Ingrese N: ").strip())

            if candidato >= 0:
                n = candidato
            else:
                print("N no puede ser negativo")
        except ValueError:
            print("Debe ingresar un número entero")

    return n


def main() -> None:
    """
    Contrato: Ejecuta el programa principal, pide un número n y muestra la suma de los n primeros números naturales

    Precondición: El archivo debe ejecutarse como programa principal

    Postcondición: Muestra la suma o un aviso si n es demasiado grande para usar recursión
    """
    print("Suma de los N primeros números naturales")

    n = _ingresar_n()

    try:
        print(f"La suma de los {n} primeros números naturales es {_suma_naturales(n)}")
    except RecursionError:
        print("N es demasiado grande para usar recursión")


main()
