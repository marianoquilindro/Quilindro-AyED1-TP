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


def _sumar_dias(fecha: tuple, n: int) -> tuple:
    """
    Contrato: Suma n días a una fecha, avanzando de mes o año si es necesario

    Precondición: fecha debe ser una tupla (dia, mes, año) váñoda y n un número entero mayor o igual a 0

    Postcondición: Devuelve la nueva fecha como tupla (día, mes, año)
    """
    dia, mes, anio = fecha

    while n > 0:
        restantes_en_mes = _dias_del_mes(mes, anio) - dia

        if n <= restantes_en_mes:
            dia += n
            n = 0
        else:
            n -= restantes_en_mes + 1
            dia = 1
            mes += 1

            if mes > 12:
                mes = 1
                anio += 1

    return (dia, mes, anio)


def _horario_valido(horario: tuple) -> bool:
    """
    Contrato: Verifica que una tupla (horas, minutos, segundos) represente un horario correcto

    Precondición: horario debe ser una dupla de tres números enteros

    Postcondición: Devuelve True si las horas están entre 0 y 23, y los minutos si segundos entre 0 y 59, sino devuelve False
    """
    horas, minutos, segundos = horario

    return 0 <= horas <= 23 and 0 <= minutos <= 59 and 0 <= segundos <= 59


def _ingresar_horario() -> tuple:
    """
    Contrato: Solicita un horario en formato HH:MM:SS hasta que sea un horario válido

    Precondición: -

    Postcondición: Devuelve el horario ingresado como tupla (horas, minutos, segundos)
    """
    horario = ""

    while horario == "":
        entrada = input("Ingrese un horario (HH:MM:SS): ").strip()

        try:
            partes = entrada.split(":")

            if len(partes) != 3:
                raise ValueError("Cantidad de partes incorrectas")

            horario_candidato = (int(partes[0]), int(partes[1]), int(partes[2]))

            if _horario_valido(horario_candidato):
                horario = horario_candidato
            else:
                print("El horario no es correcto")

        except ValueError:
            print("Formato inválido (ej. válido: 08:30:45)")

    return horario


def _horario_a_segundos(horario: tuple) -> int:
    """
    Contrato: Convierte un horario en la cantidad de segundos transcurridos desde las 00:00:00

    Precondición: horario debe ser una tupla (horas, minutos, segundos) válida

    Postcondición: Devuelve la cantidad de segundos desde las 00:00:00
    """
    horas, minutos, segundos = horario

    return horas * 3600 + minutos * 60 + segundos


def _diferencia_horarios(horario1: tuple, horario2: tuple) -> tuple:
    """
    Contrato: Calcula la diferencia entre dos horarios, si el primero es mayor que el segundo se considera que el primero corresponde al día anterior

    Precondición: horario1 y horario2 deben ser tuplas (horas, minutos, segundos) válidas

    Postcondición: Devuelve la diferencia como tupla (horas, minutos, segundos)
    """
    segundos1 = _horario_a_segundos(horario1)
    segundos2 = _horario_a_segundos(horario2)

    if segundos1 > segundos2:
        segundos2 += 24 * 3600

    diferencia = segundos2 - segundos1

    return (diferencia // 3600, diferencia % 3600 // 60, diferencia % 60)


def _ingresar_dias() -> int:
    """
    Contrato: Solicita una cantidad de días a sumar hasta que sea un número entero mayor o igual a 0

    Precondición: -

    Postcondición: Devuelve la cantidad de días ingresado
    """
    dias = -1

    while dias < 0:
        try:
            dias = int(input("Cantidad de días a sumar: ").strip())

            if dias < 0:
                print("DEbe ser un número mayor o igual a 0")

        except ValueError:
            print("Debe ingresar un número entero")

    return dias


def main() -> None:
    """
    Contrato: Ejecuta el programa principal, suma n dias a una fecha ingresada y calcula la diferencia entre dos horarios ingresados

    Precondición: El archivo debe ejecutarse como programa principal

    Postcondición: Muestra la nueva fecha y la diferencia entre los horarios
    """
    print("Fechas y horarios con tuplas")

    print("Suma de días a una fecha")
    fecha = _ingresar_fecha()
    dias = _ingresar_dias()

    dia, mes, anio = _sumar_dias(fecha, dias)

    print(f"Sumando {dias} días a la fecha se obtiene: {dia}/{mes}/{anio}")

    print("Diferencia entre dos horarios")
    horario1 = _ingresar_horario()
    horario2 = _ingresar_horario()

    horas, minutos, segundos = _diferencia_horarios(horario1, horario2)

    print(f"La diferencia es de {horas}:{minutos}:{segundos}")


main()
