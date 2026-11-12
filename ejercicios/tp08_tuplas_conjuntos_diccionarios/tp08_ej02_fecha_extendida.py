anio_corte = 30
meses = (
    "Enero",
    "Febrero",
    "Marzo",
    "Abril",
    "Mayo",
    "Junio",
    "Julio",
    "Agosto",
    "Septiembre",
    "Octubre",
    "Noviembre",
    "Diciembre",
)


def _expandir_anio(anio: int) -> int:
    """
    Contrato: Convierte un año de dos digitos en un año de cuatro digitos seguin el año de corte, los menores o iguales al año de corte pertenecen al siglo 2000 y los mayores al siglo 1900

    Precondición: anio debe ser un número entero mayor o igual a 0

    Postondición: Devuelve el año con cuatro digitos
    """

    if anio < 100:
        if anio <= anio_corte:
            anio_completo = 2000 + anio
        else:
            anio_completo = 1900 + anio
    else:
        anio_completo = anio

    return anio_completo


def _es_bisiesto(anio: int) -> bool:
    """
    Contrato: Determina si un año es bisiesto

    Precondición: anio debe ser un número entero mayor o igual a 1

    Postcondición: Devuelve True si el año es bisiesto, False si no lo es
    """
    return anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)


def _dias_del_mes(mes: int, anio: int) -> int:
    """
    Contrato: Devuelve la cantidad de días que tiene un mes en un año dado, teniendo en cuenta años bisiestos

    Precondición: mes debe ser un entero positivo entre 1 y 12 y anio un entero mayor o igual a 1

    Postcondición: Devuelve la cantidad de días del mes
    """
    dias_por_mes = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

    dias = dias_por_mes[mes - 1]

    if mes == 2 and _es_bisiesto(anio):
        dias = 29

    return dias


def _fecha_valida(fecha: tuple) -> bool:
    """
    Contrato: Verifica que una tupla represente una fecha existente en el calendario

    Precondición: fecha debe ser una tupla de tres números enteros (día, mes, año)

    Postcondición: Devuelve True si la fecha es válida, False si no lo es
    """
    dia, mes, anio = fecha

    valida = False

    if anio >= 1 and 1 <= mes <= 12:
        valida = 1 <= dia <= _dias_del_mes(mes, anio)

    return valida


def _fecha_en_formato_extendido(fecha: tuple) -> str:
    """
    Contrato: Devuelve una fecha en formato extendido interpretando los años de dos digitos segun el año de corte definido

    Precondición: fecha debe ser una tupla (dia, mes, año) válida, con el año de dos o cuatro digitos

    Postcondición: Devuelve un string con el día, el nombre del mes y el año de cuatro dígitos
    """
    dia, mes, anio = fecha

    anio_completo = _expandir_anio(anio)

    return str(dia) + " de " + meses[mes - 1] + " de " + str(anio_completo)


def _ingresar_fecha() -> tuple:
    """
    Contrato: Solicita una fecha en formato DD/MM/AAAA hasta que sea una fecha válida

    Precondición: -

    Postcondición: Devuelve la fecha ingresada como tupla
    """
    fecha = ""

    while fecha == "":
        entrada = input("Ingrese una fecha (DD/MM/AAAA): ").strip()

        try:
            partes = entrada.split("/")

            if len(partes) != 3:
                raise ValueError("Cantidad de partes incorrectas")

            fecha_candidata = (int(partes[0]), int(partes[1]), int(partes[2]))

            if _fecha_valida(fecha_candidata):
                fecha = fecha_candidata
            else:
                print("La fecha no existe en el calendario")

        except ValueError:
            print("Formato inválido (ej. válido: 31/10/2003)")

    return fecha


def main() -> None:
    """
    Contrato: Ejecuta el programa principal, solicita una fecha y la convierte en formato extendida

    Precondición: El archivo debe ejecutarse como programa principal

    Postcondición: Muestra el resultado del uso de las funciones
    """
    print("Fecha en formato extendido")
    print(f"Año de corte para años de dos dígitos: {anio_corte}")

    fecha = _ingresar_fecha()
    texto = _fecha_en_formato_extendido(fecha)

    print(f"Fecha en formato extendido: {texto}")


main()
