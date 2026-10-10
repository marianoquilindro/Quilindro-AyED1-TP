def _filtrar_palabras_ciclos(cadena: str, n: int) -> str:
    """
    Contrato: Devuelve una cadena con las palabras que tengan n o más caracteres, usando bucles for

    Precondición: cadena debe ser una cadena de strings y n un entero positivo

    Postcondición: Devuelve un string con las palabras filtradas y separadas por espacios
    """

    palabras = cadena.split()
    palabras_filtradas = []

    for palabra in palabras:
        if len(palabra) >= n:
            palabras_filtradas.append(palabra)

    return " ".join(palabras_filtradas)


def _filtrar_palabras_comprension(cadena: str, n: int) -> str:
    """
    Contrato: Devuelve una cadena con las palabras que tengan n o más caracteres, usando listas por comprensión

    Precondición: cadena debe ser una cadena de strings y n un entero positivo

    Postcondición: Devuelve un string con las palabras filtradas y separadas por espacios
    """

    palabras = cadena.split()
    palabras_filtradas = [palabra for palabra in palabras if len(palabra) >= n]

    return " ".join(palabras_filtradas)


def _filtrar_palabras_filter(cadena: str, n: int) -> str:
    """
    Contrato: Devuelve una cadena con las palabras que tengan n o más caracteres, usando filter

    Precondición: cadena debe ser una cadena de strings y n un entero positivo

    Postcondición: Devuelve un string con las palabras filtradas y separadas por espacios
    """

    palabras = cadena.split()
    palabras_filtradas = list(filter(lambda palabra: len(palabra) >= n, palabras))

    return " ".join(palabras_filtradas)


def main() -> None:
    """ "
    Contrato: Ejecuta el programa principal, solicita una frase y un entero y muestra el resultado de aplicar las diferentes funciones

    Precondición: El archivo debe ejecutarse como programa principal

    Postcondición: Muestra el resultado de cada función
    """

    print("Filtrado de palabras por longitud")

    frase = input("Ingrese una frase: ")
    n = int(input("Ingrese la longitud mínima de las palabras:"))

    print(f"1) con bucles for: {_filtrar_palabras_ciclos(frase,n)}")
    print(f"2) con listas por comprensión: {_filtrar_palabras_comprension(frase,n)}")
    print(f"3) con filter: {_filtrar_palabras_filter(frase,n)}")


main()
