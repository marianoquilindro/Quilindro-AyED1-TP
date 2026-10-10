def _separar_claves(clave: int) -> tuple[int, int]:
    """
    Contrato: Separa la clave en dos, una formada por los dígitos que estan en posiciones impares y otra fotmada por los que estan en posiciones pares, numerando de izquierda a derecha

    Precondición: clave debe ser un entero positivo

    Postcondición: Devuelve una tupla con las dos claves obtenidas, el primer elemento corresponde a la clave formada por los digitos en posición impar, y la segunda por los de posición par

    """
    cadena_clave = str(clave)
    clave1 = ""
    clave2 = ""

    for i, elemento in enumerate(cadena_clave, start=1):
        if i % 2 != 0:
            clave1 += elemento
        else:
            clave2 += elemento

    return int(clave1), int(clave2)


def main() -> None:
    """
    Contrato: Ejecuta el programa principal, solicita una clave y muestra las claves obtenidas

    Precondición: El archivo debe ejecutarse como programa principal

    Postcondición: Muestra las dos claves obtenidas

    """

    print("Separación de claves")

    claves_juntas = int(input("Ingrese la clave: "))

    clave1, clave2 = _separar_claves(claves_juntas)

    print(f"Clave: {claves_juntas}")
    print(f"Clave 1: {clave1}")
    print(f"Clave 2: {clave2}")


main()
