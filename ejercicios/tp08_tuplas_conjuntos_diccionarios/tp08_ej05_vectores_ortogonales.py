def _calcular_producto_escalar(vector1: tuple, vector2: tuple) -> float:
    """
    Contrato: Calcula el producto escalar de dos vectores, es la suma de los productos de sus componentes

    Precondición: vector1 y vector2 deben ser tuplas de números reales

    Postcondición: Devuelve el producto como número real
    """
    x1, y1 = vector1
    x2, y2 = vector2

    return x1 * x2 + y1 * y2


def _son_ortogonales(vector1: tuple, vector2: tuple) -> bool:
    """
    Contrato: Determina si dos vectores son ortongonales, si su producto escalar es igual a 0 son ortogonales

    Precondición: vector1 y vector2 deben ser tuplas de números reales

    Postcondición: Devuelve True si los vectores son ortogonales, False si no lo son
    """
    return _calcular_producto_escalar(vector1,vector2) == 0


def _ingresar_vector(mensaje: str) -> tuple:
    """
    Contrato: Pide un vector en formato x,y hasta que sean números reales válidos

    Precondición: mensaje debe ser el string que se muestra al pedir el vector

    Postcondición: Devuelve el vector ingresado como tupla (x, y)
    """
    vector = None

    while vector is None:
        entrada = input(mensaje).strip()

        try:
            partes = entrada.split(",")

            if len(partes) != 2:
                raise ValueError("Cantidad de componentes incorrecta")

            vector = (float(partes[0]), float(partes[1]))
        except ValueError:
            print("Formato inválido, ingrese dos números separados por coma (ej: 2,3)")

    return vector


def main() -> None:
    """
    Contrato: Ejecuta el programa principal, pide pares de vectores y muestra el calculo de su producto escalar y si son ortogonales o no

    Precondición: El archivo debe ejecutarse como programa principal

    Postcondición: Muestra el resultado de cada verificación
    """
    print("Verificación de vectores ortogonales")

    continuar = "s"

    while continuar == "s":
        vector_a = _ingresar_vector("Ingrese el vector A: ")
        vector_b = _ingresar_vector("Ingrese el vector B: ")

        if _son_ortogonales(vector_a,vector_b):
            print("Son ortogonales")
        else:
            print("No son ortogonales")

        continuar = input("¿Continuar verificando pares? (s/n): ").strip().lower()


main()