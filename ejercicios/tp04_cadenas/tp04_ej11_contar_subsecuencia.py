def _contar_subcadena(cadena: str, subcadena: str) -> int:
    """
    Contrato: Cuenta cuantas veces se encuentra una subcadena adentro de una cadena, considerando que sus caracteres no tienen que estar necesariamente de forma consecutiva, pero si respetar el orden

    Precondición: cadena y subcadena deben ser cadenas de texto y subcadena no debe estar vacia

    Postcondición: Devuelve la cantidad de veces que se completa la subcadena al recorrer la cadena
    """

    cadena_minuscula = cadena.lower()
    subcadena_minuscula = subcadena.lower()

    contador  = 0
    posicion = 0

    for caracter in cadena_minuscula:
        if caracter == subcadena_minuscula[posicion]:
            posicion += 1

            if posicion == len(subcadena_minuscula):
                contador += 1
                posicion = 0

    return contador

def main() -> None:
    """
    Contrato: Ejecuta el programa principal, solicita una cadena y una subcadena y muestra cuantas veces se encontro la subcadena dentro de la cadena

    Precondición: El archivo debe ejecutarse como programa principal

    Postcondición: Muestra la cantidad de veces que se encontro la subcadena dentro de la cadena
    """
    print("Conteo de subcadenas")

    cadena = input("Ingrese una cadena de caracteres: ")
    subcadena = input("Ingrese la subcadena a buscar: ")

    cantidad = _contar_subcadena(cadena,subcadena)

    print(f"Cantidad encontrada: {cantidad}")

main()