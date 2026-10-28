def _nombre_mes(numero_mes: int) -> str:
    """
    Contrato: Devuelve el nombre del mes correspondiente a un número de mes, obteniendolo de una lista que esta dentro de la función

    Precondición: numero_mes debe ser un número entero

    Postcondición: Devuelve el nombre del mes o un string vacío si el número de mes es inválido
    """
    meses = [
        "enero",
        "febrero",
        "marzo",
        "abril",
        "mayo",
        "junio",
        "julio",
        "agosto",
        "septiembre",
        "octubre",
        "noviembre",
        "diciembre",
    ]

    try:
        if numero_mes < 1:
            raise IndexError
        nombre = meses[numero_mes - 1]
    except IndexError:
        nombre = ""

    return nombre


def main() -> None:
    """
    Contrato: Ejecuta el programa principal, lee números de mes hasta que se ingresa un string vacio y muestra el nombre de cada mes

    Precondición: El archivo debe ejecutarse como programa principal

    Postcondición: Muestra el nombre de cada mes ingresado, o un aviso si el número es inválido
    """
    print("Nombre del mes a partir de un número")

    entrada = input("Ingrese el número de mes (vacío para terminar): ")

    while entrada != "":
        try:
            numero_mes = int(entrada)
            nombre = _nombre_mes(numero_mes)

            if nombre == "":
                print("El número de mes no es válido")
            else:
                print(f"El mes es: {nombre}")
        except ValueError:
            print("Debe ingresar un número entero")

        entrada = input("Ingrese el número de mes (vacío para terminar): ")


main()
