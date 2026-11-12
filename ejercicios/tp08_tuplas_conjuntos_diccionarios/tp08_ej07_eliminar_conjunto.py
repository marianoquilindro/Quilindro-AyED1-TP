def _sacar_elementos(conjunto: set, valor: int) -> bool:
    """
    Contrato: Saca un valor de un conjunto usando remove

    Precondición: conjunto debe ser un conjunto de números enteros y valor un número entero

    Postcondición: Modifica el conjunto sacando el valor y devuelve True, o False si el valor no pertenece al conjunto
    """
    try:
        conjunto.remove(valor)
        sacado = True
    except KeyError:
        sacado = False

    return sacado


def main() -> None:
    """
    Contrato: Ejecuta el programa principal, genera un conjunto con números del 0 al 9 y pide valores para ir eliminando elementos del conjunto hasta que se ingresa -1 o se vacía el conjunto

    Precondición: El archivo debe ejecutarse como programa principal

    Postcondición: Muestra el contenido del conjunto luego de cada eliminación
    """
    print("Eliminación de elementos de un conjunto")

    conjunto = set(range(10))

    print(f"Conjunto inicial: {conjunto}")

    entrada = input("Ingrese un valor a eliminar (-1 para terminar): ").strip()

    while entrada != "-1" and len(conjunto) > 0:
        try:
            valor = int(entrada)

            if _sacar_elementos(conjunto, valor):
                print(f"Se saco el {valor}, Conjunto: {conjunto}")
            else:
                print(f"El valor {valor} no pertenece al conjunto")
        except ValueError:
            print("Error, debe ingresar un número entero")

        if len(conjunto) > 0:
            entrada = input("Ingrese un valor a eliminar (-1 para terminar): ").strip()

    if len(conjunto) == 0:
        print("El conjunto quedó vacío")


main()
