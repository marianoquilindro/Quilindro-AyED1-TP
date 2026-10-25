def _menor_a_cien(numero: int) -> str:
    """
    Contrato: Convierte a letras un numero entre 1 y 99

    Precondición: numero debe ser un entero entre 1 y 99

    Postcondición: Devuelve un string con el numero escrito en letras
    """
    casos_especiales = ("","uno","dos","tres","cuatro","cinco","seis","siete","ocho","nueve","diez","once","doce","trece","catorce","quince","dieciseis","diecisiete","dieciocho","diecinueve","veinte","veintiuno","veintidos","veintitres","veinticuatro","veinticinco","veintiseis","veintisiete","veintiocho","veintinueve")

    decenas = ("","","","treinta","cuarenta","cincuenta","sesenta","setenta","ochenta","noventa")

    if numero < 30:
        texto = casos_especiales[numero]
    else:
        decena = numero // 10
        unidad = numero % 10
        texto = decenas[decena]

        if unidad != 0:
            texto += " y " + casos_especiales[unidad]

    return texto


def _menor_a_mil(numero: int) -> str:
    """
    Contrato: Convierte a letras un numero entre 1 y 999

    Precondición: numero debe ser un entero entre 1 y 999

    Postcondición: Devuelve un string con el numero escrito en letras
    """
    centenas = ("","ciento","doscientos","trescientos","cuatrocientos","quininetos","seiscientos","setecientos","ochocientos","novecientos")

    if numero == 100:
        return "cien"

    centena = numero // 100
    resto = numero % 100
    texto = centenas[centena]

    if resto > 0:
        if texto != "":
            texto += " "
        texto += _menor_a_cien(resto)

    return texto


def _menor_a_un_millon(numero: int) -> str:
    """
    Contrato: Convierte a letras un numero entre 1 y 999999

    Precondición: numero debe ser un entero entre 1 y 999999

    Postcondición: Devuelve un string con el numero escrito a letras
    """
    miles = numero // 1000
    resto = numero % 1000
    texto = ""

    if miles == 1:
        texto = "mil"
    elif miles > 1:
        texto = -_menor_a_mil(miles) + "mil"

    if resto > 0:
        if texto != "":
            texto += " "
        texto += _menor_a_mil(resto)

    return texto


def _numero_a_letras(numero: int) -> str:
    """
    Contrato: Convierte a letras un numero entre 0 y 1 billon

    Precondición: numero debe ser un entero entre 0 y un billon

    Postcondición: Devuelve un string con el numero escrito a letras
    """
    billon = 1000000000000
    millon = 1000000

    if numero == 0:
        return "cero"

    if numero == billon:
        return "un billon"

    millones = numero // millon
    resto = numero % millon
    texto = ""

    if millones == 1:
        texto = "un millon"
    elif millones > 1:
        texto = _menor_a_un_millon(millones) + "millones"

    if resto > 0:
        if texto != "":
            texto += " "
        texto += _menor_a_un_millon(resto)

    return texto


def main() -> None:
    """
    Contrato: Ejecuta el programa principal, pide un numero entero y lo muestra escrito

    Precondición: El archivo debe ejecutarse como programa principal

    Postcondición: Muestra el numero convertido a letras
    """
    print("Conversion de numeros a letras")

    numero = int(input("Ingrese un numero entre 0 y un billon (1.000.000.000.000): "))
    print(f"{numero} en letras: {_numero_a_letras(numero)}")


main()