def _buscar_clave(diccionario: dict, valor: str) -> list:
    """
    Contrato: Busca todas las claves de un diccionario que estén asociadas al valor dado

    Precondición: diccionario debe ser un diccionario y valor un valor del tipo que este guardado en el diccionario

    Postcondición: Devuelve una lista con las claves asociadas al valor, o una lista vacía si no hay niguna clave asociada al valor
    """
    claves = []

    for clave, valor_asociado in diccionario.items():
        if valor_asociado == valor:
            claves.append(clave)

    return claves

def main() -> None:
    """
    Contrato: Ejecuta el programa principal, muestra un diccionario y solicita valores a buscar hasta que se ingresa un string vacío

    Precondición: El archivo debe ejecutarse como programa principal

    Postcondición: Muestra la lista de claves que apuntan a cada valor buscado
    """
    print("Búsqueda de claves por valor")

    colores = {"manzana": "roja", "frutilla": "roja", "banana": "amarilla", "uva": "violeta"}

    print(f"Diccionario (fruta: color): {colores}")

    valor = input("Ingrese un color a buscar (vacío para terminar): ").strip()

    while valor != "":
        claves = _buscar_clave(colores,valor)

        if len(claves) == 0:
            print(f"Ninguna fruta tiene el color {valor}")
        else:
            print(f"Frutas de color {valor} : {claves}")

        valor = input("Ingrese un color a buscar (vacío para terminar): ")


main()