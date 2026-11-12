def _extraer_palabras(frase: str) -> list:
    """
    Contrato: Separa una frase en una palabra, reemplaza por espacios todo lo que no sea una letra o un número

    Precondición: frase debe ser una cadena de texto

    Postcondición: Devuelve una lista con las palabras de la frase
    """
    texto = ""

    for caracter in frase.lower():
        if caracter.isalnum():
            texto += caracter
        else:
            texto += " "

    return texto.split()


def _ordenar_por_longitud(palabras: set) -> list:
    """
    Contrato: Ordena un conjunto de palabras por su longitud, de la más corta a la más larga

    Precondición: palabras debe ser un conjunto de strings

    Postcondición: Devuelve una lista con las palabras ordenadas por longitud
    """
    listado = []

    for palabra in palabras:
        listado.append([len(palabra), palabra])

    listado.sort()

    ordenadas = []

    for longitud, palabra in listado:
        ordenadas.append(palabra)

    return ordenadas


def main() -> None:
    """
    Contrato: Ejecuta el programa principal, pide una frase, elimina las palabras repetidas y juestra el resultado ordenado por longitud

    Precondición: El archivo debe ejecutarse como programa principal

    Postcondición: Muestra la cantidad de palabras y las palabras sin repetir ordenadas por longitud
    """
    print("Palabras sin repetir ordenadas por longitud")

    frase = input("Ingrese una frase: ")

    palabras = _extraer_palabras(frase)

    if len(palabras) == 0:
        print("No se ingresaron palabras")
    else:
        unicas = set(palabras)
        ordenadas = _ordenar_por_longitud(unicas)

        print(f"Palabras: ingresadas: {len(palabras)}, palabras distinas: {len(unicas)}")
        print("Palabras ordenadas por longitud:")

        for palabra in ordenadas:
            print(f"Palabra: {palabra}, longitud: {len(palabra)}")


main()
