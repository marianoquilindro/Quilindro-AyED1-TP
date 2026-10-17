def _reemplazar_palabra(cadena: str, palabra_vieja: str, palabra_nueva: str) -> tuple[str, int]:
    """
    Contrato: Reemplaza todas las apariciones de una palabra por otra en una cadena

    Precondición: cadena, palabra_vieja y palabra_nueva deben ser cadenas de texto y palabra_vieja no debe estar vacía

    Postcondición: Devuelve una tupla con la cadena resultante y la cantidad de reemplazos
    """
    palabras = cadena.split(" ")
    palabras_resultado = []
    cantidad_reemplazos = 0

    for palabra in palabras:
        if palabra == palabra_vieja:
            palabras_resultado.append(palabra_nueva)
            cantidad_reemplazos += 1
        else:
            palabras_resultado.append(palabra)

    return " ".join(palabras_resultado), cantidad_reemplazos

def main() -> None:
    """
    Contrato: Ejecuta el programa principal, solicita una cadena, la palabra a reemplazar y la palabra nueva

    Precondición: El archivo debe ejecutarse como programa principal

    Postcondición: Muestra la cadena obtenida y la cantidad de reemplazos
    """
    print("Reemplazo de palabras")

    cadena = input("Ingrese una cadena de caracteres: ")
    palabra_vieja = input("Ingrese la palabra a reemplazar: ")
    palabra_nueva = input("Ingrese la palabra nueva: ")

    resultado, cantidad = _reemplazar_palabra(cadena,palabra_vieja,palabra_nueva)

    print(f"Cadena obtenida: {resultado}")
    print(f"Cantidad de reemplazos: {cantidad}")

main()