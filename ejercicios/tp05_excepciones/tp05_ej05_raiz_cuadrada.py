import math


def _calcular_raiz(numero: float) -> float:
    """
    Contrato: Calcula la raíz de un número usando la función sqrt() del módulo math

    Precondición: numero debe ser un número real

    Postcondición: Devuelve la raíz cuadrada del número 0 -1 si el número es negativo
    """

    try:
        raiz = math.sqrt(numero)
    except ValueError:
        raiz = -1

    return raiz


def main() -> None:
    """
    Contrato: Ejecuta el programa principal, solicita números hasta que se carga un string vacío y muestra la raíz cuadrada de cada uno

    Precondición: El archivo debe ejecutarse como programa principal

    Postcondición: Muestra la raíz cuadrada de cada número ingresado o un aviso si el número es negativo o no es válido
    """
    print("Cálculo de la raíz cuadrada de un número")

    entrada = input("Ingrese un número (vacío para terminar): ")

    while entrada != "":
        try:
            numero = float(entrada)
            raiz = _calcular_raiz(numero)

            if raiz == -1:
                print("No se puede calcular la raíz cuadrada de un número negativo")
            else:
                print(f"La raíz cuadrada es: {raiz}")
        except ValueError:
            print("Debe ingresar un número válido")

        entrada = input("Ingrese un número (vacío para terminar): ")


main()
