def _ingresar_entero() -> int:
    """
    Contrato: Pide un número entero hasta que el valor ingresado sea válido

    Precondición: -

    Postcondición: Devuelve el número entero que se ingreso
    """

    numero = None

    while numero is None:
        try:
            numero = int(input("Ingrese un número entero: ").strip())
        except ValueError:
            print("Debe ingresar un número entero")

    return numero


def _generar_tabla(n: int) -> dict:
    """
    Contrato: Usando diccionarios genera una tabla de multiplicar de un número donde cada clave es un multiplicador del 1 al 12 y su valor es el producto de n por la clave

    Precondición: n debe ser un número entero

    Postcondición: Devuelve un diccionario con doce pares de multiplicador: producto
    """
    return {multiplicador: n * multiplicador for multiplicador in range(1, 13)}


def main() -> None:
    """
    Contrato: Ejecuta el programa principal, pide un número entero y genera su tabla de multiplicar del 1 al 12

    Precondición: El archivo debe ejecutarse como programa principal

    Postcondición: Muestra la tabla de multiplicar del número ingresado
    """
    print("Tabla de multiplicar")

    n = _ingresar_entero()
    tabla = _generar_tabla(n)

    print(tabla)


main()
