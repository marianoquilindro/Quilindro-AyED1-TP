def _esbisiesto(anio: int) -> bool:
    """
    Contrato: Determina si un año es bisiesto
    
    Precondiciones: anio debe ser un entero positivo

    Postcondiciones: Devuelve True si el año es bisiesto y False si no lo es

    """
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

def _dias_del_mes (mes: int, anio: int) -> int:
    """
    Contrato: Devuelve la cantidad de días que tiene un mes, teniendo en cuenta si el año es bisiesto

    Precondicion: mes debe ser un entero entr 1 y 12, anio debe ser un entero positivo
    
    Postcondiciones: Devuelve la cantidad de días del mes

    """
    treinta = [4,6,9,11]

    if mes in treinta:
        dias = 30
    elif mes == 2:
        if _esbisiesto(anio):
            dias = 29
        else:
            dias = 30
    else:
        dias = 31

    return dias

def _diasiguiente (dia: int, mes: int, anio: int) -> tuple [int,int,int]:
    """
    Contrato: Calcula la fecha del día siguiente a la fecha recibida

    Precondiciones: dia, mes y anio deben formar una fecha válida

    Postcondiciones: Devuelve una tupla (dia, mes, anio) correspondiente al dia siguiente
    
    """

    if dia < _dias_del_mes(mes, anio):
        return dia +1, mes, anio
    elif mes < 12:
        return 1, mes +1, anio
    else:
        return 1, 1, anio +1

def _es_fecha_anterior (dia1: int, mes1: int, anio1:int, dia2: int, mes2: int, anio2: int) -> bool:
    """
    Contrato: Determina si la primera fecha es anterior a la segunda
    
    Precondicion: Ambas fechas deben ser válidas

    Postcondicion: Devuelve True si la primer fecha es anterior a la segunda, False si es al reves
    
    """
    if anio1 != anio2:
        return anio1 < anio2
    elif mes1 != mes2:
        return mes1 < mes2
    else:
        return dia1 < dia2


def _sumar_dias (dia: int, mes: int, anio: int, cantidad_dias: int) -> tuple [int,int,int]:
    """
    Contrato: Suma una cantidad de días a una fecha

    Precondicion: dia, mes y anio deben ser una fecha válida, cantidad_dias debe ser un entero positivo o cero
    
    Postcondiciones: Devuelve una tupla con la fecha que se obtiene

    """
    dia_actual = dia
    mes_actual = mes
    anio_actual = anio

    contador = 0

    while contador < cantidad_dias:
        fecha_siguiente = _diasiguiente(dia_actual, mes_actual, anio_actual)
        dia_actual = fecha_siguiente[0]
        mes_actual = fecha_siguiente[1]
        anio_actual = fecha_siguiente[2]
        contador += 1

        return dia_actual, mes_actual, anio_actual


def _dias_entre_fechas (dia1: int, mes1: int, anio1: int, dia2: int, mes2: int, anio2: int) -> int:
    """
    Contrato: Calcula la cantidad de días que existen entre dos fechas ingresadas por el usuario sin  importar el orden de ingreso

    Precondicion: Ambas fechas deben ser válidas

    Postcondicion: Devuelve la cantidad de días entra ambas fechas
    
    """

    if _es_fecha_anterior (dia1, mes1, anio1, dia2, mes2, anio2):
        dia_actual = dia1
        mes_actual = mes1
        anio_actual = anio1
        dia_final = dia2
        mes_final = mes2
        anio_final = anio2
    else:
        dia_actual = dia2
        mes_actual = mes2
        anio_actual = anio2
        dia_final = dia1
        mes_final = mes1
        anio_final = anio1

    contador = 0
    while dia_actual != dia_final or mes_actual != mes_final or anio_actual != anio_final:
        fecha_siguiente = _diasiguiente (dia_actual, mes_actual, anio_actual)
        dia_actual = fecha_siguiente[0]
        mes_actual = fecha_siguiente[1]
        anio_actual = fecha_siguiente[2]
        contador += 1

    return contador


def main() -> None:
    """
    Contrato: Ejecuta el programa principal, permite sumar n cantidad de días a una fecha y calcular la cantidad de días entre dos fechas

    Precondicion: El archivo debe ejecutarse como programa principal

    Postcondicion: Muestra los resultados de ambas operaciones
    
    """

    print("Sumar n días a una fecha")
    dia = int(input("Ingrese el día: "))
    mes = int(input("Ingrese el mes: "))
    anio = int(input("Ingrese el año: "))
    cant_dias = int(input("Ingrese la cantidad de días a sumar: "))

    dia_resultado, mes_resultado, anio_resultado = _sumar_dias(dia, mes, anio, cant_dias)
    print(f"La fecha resultante es {dia_resultado}/{mes_resultado}/{anio_resultado}")


    print("Calcular días entre dos fechas")
    dia1 = int(input("Ingrese el día de la primera fecha: "))
    mes1 = int(input("Ingrese el mes de la primera fecha: "))
    anio1 = int(input("Ingrese el año de la primera fecha: "))
    dia2 = int(input("Ingrese el día de la segunda fecha: "))
    mes2 = int(input("Ingrese el mes de la segunda fecha: "))
    anio2 = int(input("Ingrese el año de la segunda fecha: "))

    dias_entre = _dias_entre_fechas(dia1, mes1, anio1, dia2, mes2, anio2)
    print(f"Entre las dos fechas hay {dias_entre} días")

main()