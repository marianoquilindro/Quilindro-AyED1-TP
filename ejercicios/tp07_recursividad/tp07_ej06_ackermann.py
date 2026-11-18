def _ackermann(m: int, n: int) -> int:
    """
    Contrato: Calcula recursivamente la función ackermann

    Precondición: m y n deben ser números enteros mayores o iguales a 0

    Postcondición: Devuelve el valor de A(m, n)
    """
    if m == 0:
        resultado = n + 1
    elif n == 0:
        resultado = _ackermann(m - 1, 1)
    else:
        resultado = _ackermann(m - 1, _ackermann(m, n - 1))

    return resultado


def main() -> None:
    """
    Contrato: Ejecuta el programa principal, muestra un cuadro con los valores de la función ackermann, usando un guion en los valores que superan el limite de recursion

    Precondición: El archivo debe ejecutarse como programa principal

    Postcondición: Muestra el cuadro de valores
    """
    print("Valores de la función Ackermann")

    encabezado = "\m\n"

    for n in range(8):
        encabezado += f"{n:>6}"

    print(encabezado)

    for m in range(4):
        fila = f"{m:>3}"

        for i in range(8):
            try:
                valor = _ackermann(m, n)
            except RecursionError:
                valor = "-"

            fila += f"{valor:>6}"

        print(fila)


main()
