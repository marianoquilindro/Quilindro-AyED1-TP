maximo_puntos = 6


def _encajan(ficha1: tuple, ficha2: tuple) -> bool:
    """
    Contrato: Determina si dos fichas de dominó encajan, osea si tiene al menos un número en común

    Precondición: ficha1 y ficha2 deben ser tuplas de dos números enteros

    Postcondición: Devuelve True si las fichas tiene algún número en común, o False si no
    """
    comunes = set(ficha1) & set(ficha2)

    return len(comunes) > 0


def _ingresar_ficha(mensaje: str) -> tuple:
    """
    Contrato: Solicita una ficha de dominón en formtao A,B hasta que sean dos números enterso entre 0 y el máximo de puntos de la ficha

    Precondición: mensaj debe ser la cadena que se muestra al pedir la ficha

    Postcondición: Devuelve la ficha ingresada como tupla de dos números enteros
    """
    ficha = ""

    while ficha == "":
        entrada = input(mensaje).strip()

        try:
            partes = entrada.split(",")

            if len(partes) != 2:
                raise ValueError("Cantidad de números incorrecta")

            ficha_candidata = (int(partes[0]), int(partes[1]))

            if (
                0 <= ficha_candidata[0] <= maximo_puntos
                and 0 <= ficha_candidata[1] <= maximo_puntos
            ):
                ficha = ficha_candidata
            else:
                print(f"Los números deben estar entre 0 y {maximo_puntos}")
        except ValueError:
            print("Formato inválido. Ingrese los números separados por coma (ej: 3,4)")

    return ficha


def main() -> None:
    """
    Contrato: Ejecuta el programa principal, solicita pares de fichas de dominó y muestra si encajan o no

    Precondición: El archivo debe ejecutarse como programa principal

    Postcondición: Muestra el resultado de cada verificación
    """
    print("Verificación de fichas de dominó")

    continuar = "s"

    while continuar == "s":
        ficha1 = _ingresar_ficha("Ingrese la primera ficha (A,B): ")
        ficha2 = _ingresar_ficha("Ingrese la segunda ficha (A,B): ")

        if _encajan(ficha1, ficha2):
            print(f"Las fichas {ficha1} y {ficha2} encajan")
        else:
            print(f"Las fichas {ficha1} y {ficha2} no encajan")

        continuar = input("¿Verificar otro par? (s/n): ").strip().lower()


main()
