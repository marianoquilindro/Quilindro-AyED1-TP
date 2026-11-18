def _mcd(x: int, y: int) -> int:
    """
    Contrato: Calcula el maximo común divisor de dos números enteros no negativos usando recursión

    Precondición: x e y deben ser números enteros mayores o iguales a 0

    Postcondición: Devuelve el máximo común divisor de x e y
    """
    if y == 0:
        resultado = x
    elif x == 0:
        resultado = y
    elif x == y:
        resultado = x
    elif x > y:
        resultado = -_mcd(x - y, y)
    else:
        resultado = _mcd(y, x)

    return resultado


def _mcd_lista(numeros: list) -> int:
    """
    Contrato: Calcula el maximo común divisor de todos los elementos de una lista usando recursión

    Precondición: numeros debe ser una lista con al menos un elemento y que los elementos sean números enteros mayores o iguales a 0

    Postcondición: Devuelve el maximo común divisor de todos los elementos de la lista
    """
    if len(numeros) == 1:
        resultado = numeros[0]
    else:
        resultado = _mcd(_mcd_lista(numeros[:-1]), numeros[-1])

    return resultado


def _leer_numeros() -> list:
    """
    Contrato: Pide números enteros no negativos de a uno usando recursividad hasta que se ingresa una cadena vacía

    Precondición: -

    Postcondición: Devuelve la lista con los números ingresados
    """
    entrada = input(
        "Ingrese un número entero no negativo (vacío para terminar): "
    ).strip()

    if entrada == "":
        numeros = []
    else:
        try:
            numero = int(entrada)
        except ValueError:
            numero = -1

        if numero < 0:
            print("Debe ingresar un número entero no negativo")
            numeros = _leer_numeros()
        else:
            numeros = [numero] + _leer_numeros()

    return numeros


def main() -> None:
    """
    Contrato: Ejecuta el programa principal, lee una lista de números y muestra el maximo común divisor de todos

    Precondición: El archivo debe ejecutarse como programa principal

    Postcondición: Muestra el maximo común divisor de la lista o un aviso si los números son muy grandes para resolverlo con recursión
    """
    print("Máximo común divisor de una lista de números")

    numeros = _leer_numeros()

    if len(numeros) == 0:
        print("No se ingresaron números")
    else:
        try:
            print(f"El máximo común divisor de {numeros} es {_mcd_lista(numeros)}")
        except RecursionError:
            print("Los números son muy grandes para resolverlo con recursión")


main()
