def _generar_cuadrados(inicio: int, fin: int) -> dict:
    """
    Contrato: Genera un diccionario en el que las claves son los números enteros entre inicio y fin y donde los valores son el cuadrado de cada clave

    Precondición: desde y hasta deben ser números enteros con inicio mayor o igual a fin

    Postcondición: Devuelve el diccionario con un par clave: cuadrado por cada número del rango
    """
    cuadrados = {}

    for numero in range(inicio, fin + 1):
        cuadrados[numero] = numero**2

    return cuadrados


def main() -> None:
    """
    Contrato: Ejecuta el programa principal, genera un diccionario con los números del 1 al 20

    Precondición: El archivo debe ejecutarse como programa principal

    Postcondición: Muestra el diccionario generado
    """
    print("Diccionario de cuadrados del 1 al 20")

    cuadrados = _generar_cuadrados(1, 20)

    print(cuadrados)


main()
