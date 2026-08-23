def _esbisiesto(anio: int) -> bool:
    """
    Contrato: Determina si un año es bisiesto
    
    Precondiciones: anio debe ser un entero positivo

    Postcondiciones: Devuelve True si el año es bisiesto y False si no lo es

    """
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)


def _es_fecha_valida(dia: int, mes: int, anio: int) -> bool:
    """
    Contrato: Verifica si las variables dia, mes y anio forman una fecha válida considerando los dias de cada mes y los años bisiestos

    Precondiciones: dia, mes y anio deben ser enteros positivos

    Postcondiciones: Devuelve True si la fecha es válida o False si no lo es
    
    """
    treinta = [4,6,9,11]

    if anio >= 1:
        anio_valido = True
    else:
        anio_valido = False

    if mes >= 1 and mes <= 12:
        mes_valido = True
    else:
        mes_valido = False


    if not mes_valido:
        return False

    if mes in treinta:
        dia_limite = 30
    elif mes == 2:
        dia_limite = 29 if _esbisiesto(anio) else 28
    else:
        dia_limite = 31

    if dia >= 1 and dia <= dia_limite:
        dia_valido  = True
    else:
        dia_valido = False

    return dia_valido and mes_valido and anio_valido

def main () -> None:
    """
    Contrato: Ejecuta el programa principal, solicita una fecha y muestra si es válida o no

    Precondiciones: Debe ejecutarse como programa principal

    Postcondiciones: Muestra si la fecha ingresada es válida
    
    """
    print("Verificación de fecha válida")

    dia = int(input("Ingrese el dia: "))
    mes = int(input("Ingrese el mes: "))
    anio = int(input("Ingrese el año: "))

    if _es_fecha_valida (dia, mes, anio):
        print(f"la fecha {dia}/{mes}/{anio} es válida")
    else:
        print(f"la fecha {dia}/{mes}/{anio} no es válida")

main()
    