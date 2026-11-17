def _contar_vocales(palabra: str) -> dict:
    """
    Contrato: Cuenta las vocales de una palabra, teniendo en cuenta las tildes

    Precondición: palabra debe ser una cadena de texto

    Postcondición: Devuelve un diccionario en el que las claves son las vocales (a, e, i, o, u) y el valor es la cantidad de veces que aparece cada una
    """
    conteo = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
    vocales = {"á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u"}

    for letra in palabra.lower():
        if letra in vocales:
            letra = vocales[letra]

        if letra in conteo:
            conteo[letra] += 1

    return conteo

def _extraer_palabras(frase: str) -> list:
    """
    Contrato: Separa una frase en palabras en minúsculas, reemplaza por espacios todo lo que no sea una letra o un número

    Precondición: frese debe ser una cadena de texto

    Postcondición: Devuelve la lista de palabras de la frase
    """
    texto = ""

    for caracter in frase.lower():
        if caracter.isalnum():
            texto += caracter
        else:
            texto += " "

    return texto.split()


def main() -> None:
    """
    Contrato: Ejecuta el programa principal, pide una frase y luego la mustra junto a la cantidad de cada vocal hayada

    Precondición: El archivo debe ejecutarse como programa principal

    Postcondición: Muestra la cantidad de vocales de cada palabra de la frase
    """
    print("Conteo de vocales")

    frase = input("ingrese una frase: ")

    palabras = _extraer_palabras(frase)

    if len(palabras) == 0:
        print("No se ingresaron palabras")
    else:
        for palabra in palabras:
            conteo = _contar_vocales(palabra)

            detalle = ""

            for vocal, cantidad  in conteo.items():
                if cantidad > 0:
                    if detalle != "":
                        detalle += ", "

                    detalle += vocal + "=" + str(cantidad)

            total = sum(conteo.values())

            if total == 0:
                print(f"{palabra}: no tiene vocales")
            else:
                print(f"{palabra}: {detalle} (total: {total})")



main()