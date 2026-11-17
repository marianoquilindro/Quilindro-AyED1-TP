def _eliminar_claves(diccionario: dict, claves: list) -> tuple:
    """
    Contrato: Elimina de un diccionario todas las claves de una lista

    Precondición: diccionario debe ser un diccionario y claves una lista de claves posibles

    Postcondición: Modifica el diccionario que recibe y devuelve una tupla con el diccionario modificado y la cantidad de claves eliminadas
    """
    eliminadas = 0

    for clave in claves:
        try:
            del diccionario[clave]
            eliminadas += 1
        except KeyError:
            pass

    return (diccionario, eliminadas)


def main() -> None:
    """
    Contrato: Ejecuta el programa principal, muestra un diccionario, pide claves a eliminar y muestra el diccionario modificado y la cantidad de claves eliminadas

    Precondición: El archivo debe ejecutarse como programa principal

    Postcondición: Muestra el diccionario original, el modificado y la cantidad de claves eliminadas
    """
    print("Eliminación de claves de un diccionario")

    edades = {"ana": 25, "luis": 31, "marta": 28, "pedro": 40, "sofia": 22}

    print(f"Diccionario original: {edades}")

    entrada = input("Ingrese las claves a eliminar separadas por coma: ")

    claves = []

    for parte in entrada.split(","):
        clave = parte.strip()

        if clave != "":
            claves.append(clave)

    edades, cantidad = _eliminar_claves(edades, claves)

    print(f"Diccionario modificado: {edades}")
    print(f"Claves eliminadas: {cantidad}")

main()