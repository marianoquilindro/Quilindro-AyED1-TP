def _convertir_romano(numero: int) -> str:
    """
    Contrato: Convierte un número entero que este entre 0 y 3999 a número romano

    Precondición: numero debe ser un entero entre 0 y 3999

    Postcondición: Devuelve una string con el número representado en romano

    """

    valores = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    simbolos = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

    resultado = ""
    indice = 0

    while indice < len(valores):
        while numero >= valores[indice]:
            resultado += simbolos[indice]
            numero -= valores[indice]
        indice += 1

    return resultado


def main() -> None:
    """
    Contrato: Ejecuta el programa principal, solicita un número y muestra como quedaria en números romanos

    Precondición: El archivo debe ejecutarse como programa principal

    Postcondición: Muestra el resultado del número convertido a romano

    """

    print("Conversión a número romano")

    numero = int(input("Ingrese un número entre 0 y 3999: "))

    print(f"{numero} en números romanoe es: {_convertir_romano(numero)}")


main()
