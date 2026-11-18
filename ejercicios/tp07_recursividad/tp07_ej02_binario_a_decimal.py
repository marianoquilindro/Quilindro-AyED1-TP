def _es_binario(numero: int) -> bool:
    """
    Contrato: Verifica que todas las cifras de un número sean 0 o 1 de manera recursiva

    Precondición: numero debe ser un número entero mayor o igual a 0

    Postcondición: Devuelve True si el número solo tiene cifras 0 y 1, o False en caso contrario
    """
    if numero == 0:
        binario = True
    elif numero % 10 > 1:
        binario = False
    else:
        binario = _es_binario(numero // 10)

    return binario


def _binario_a_decimal(binario: int) -> int:
    """
    Contrato: Convierte un número binario a base decimal de manera recursiva

    Precondición: binario debe ser un número entero mayor o igual a 0 formado por 0 y 1

    Postcondición: Devuelve el valor del número en base decimal
    """
    if binario == 0:
        decimal = 0
    else:
        decimal = binario % 10 + 2 * _binario_a_decimal(binario // 10)

    return decimal


def _ingresar_binario() -> int:
    """
    Contrato: Pide un número binario hasta que sea válido

    Precondición: -

    Postcondición: Devuelve el número binario ingresado como número entero
    """
    binario = None

    while binario is None:
        try:
            candidato = int(input("Ingrese un número binario (solo 0 y 1): ").strip())

            if candidato >= 0 and _es_binario(candidato):
                binario = candidato
            else:
                print("Un número binario solo debe tener las cifras 0 y 1")
        except ValueError:
            print("Debe ingresar un número entero")

    return binario


def main() -> None:
    """
    Contrato: Ejecuta el programa principal, pide un número binario y muestra su valor en base decimal

    Precondición: El archivo debe ejecutarse como programa principal

    Postcondición: Muestra el número convertido a base decimal
    """
    print("Conversión de binario a decimal")

    binario = _ingresar_binario()

    print(
        f"El número binario {binario} equivale a {_binario_a_decimal(binario)} en base decimal"
    )


main()
