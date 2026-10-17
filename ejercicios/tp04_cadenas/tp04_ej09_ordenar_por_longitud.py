def _longitud_sin_puntuacion(palabra: str) -> int:
    """
    Contrato: Calcula la longitud de una palabra sin contar los signos de puntuación

    Precondición: palabra debe ser una cadena de texto

    Postcondición: Devuelve la cantidad de caracteres de una palabra que son letras o numeros
    """
    contador = 0

    for caracter in palabra:
        if caracter.isalnum():
            contador += 1

    return contador


def _ordenar_palabras(cadena: str) -> str:
    """
    Contrato: Devuelve una cadena con las palabras de la frase ordenadas de menor a mayor segun su longitud, sin tener en cuenta los signos de puntuación

    Precondición: cadena debe ser una cadena de texto con las palabras separadas por uno o mas espacios

    Postcondición: Devuelve una cadena con las palabras ordenadas por longitud espaciadas entre cada una
    """
    palabras = cadena.split()
    palabras_ordenadas = sorted(palabras, key= _longitud_sin_puntuacion)

    return " ".join(palabras_ordenadas)

def main() -> None:
    """
    Contrato: Ejecuta el programa principal, solicita una frase y muestra sus palabras ordenadas por longitud

    Postcondición: El archivo debe ejecutarse como programa principal

    Precondición: Muestra la frase ordenada por longitud
    """

    print("Ordenamiento de palabras por longitud")

    frase = input("Ingrese una frase: ")

    print(f"Frase ordenada: {_ordenar_palabras(frase)}")

main()