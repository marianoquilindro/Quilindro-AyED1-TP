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


def _diadelasemana (dia: int, mes:int, anio: int) -> int:
    """
    Contrato: Calcula el día de la semana correspondiente a una fecha

    Precondiciones: dia, mes y anio deben formar una fecha válida
    
    Postcondiciones: Devuelve 0 para domingo, 1 para lunes, 2 para martes ....

    """

    if mes < 3:
        mes = mes + 10
        anio = anio -1
    else:
        mes = mes - 2

    siglo = anio // 100
    anio2 = anio % 100
    diasem = (((26 * mes - 2) // 10) + dia + anio2 + (anio2 // 4) + (siglo // 4) - (2 * siglo)) % 7

    if diasem < 0:
        diasem = diasem + 7

    return diasem

def _nombre_dia (dia_semana: int) -> str:
    """
    Contrato: Devuelve el nombre abreviado del día de la semana correspondiente a un número
    
    Precondiciones: dia_semana debe estar entre 0 y 6

    Postcondiciones: Devuelve un string con el nombre del día abreviado

    """

    dias = ("Dom", "Lun", "Mar", "Mié", "Jue", "Vie", "Sáb")
    return dias[dia_semana]


def main() -> None:
    """
    Contrato: Ejecuta el programa principal, solicita un mes y año y muestra el calendario completo del mes
    
    Precondiciones: El archivo debe ejecutarse como programa principal

    Postcondiciones: Muestra el calendario del mes y año ingresados
    
    """

    mes = int(input("Ingrese el mes: "))
    anio = int(input("Ingrese el año: "))

    encabezado = ""
    for dia_semana in range(0, 7):
        encabezado += _nombre_dia(dia_semana) + "\t"
    print(encabezado)
 
    primer_dia_semana = _diadelasemana(1, mes, anio)
    dias_mes = _dias_del_mes(mes, anio)
 
    
    contador_columna = 0
 
    
    while contador_columna < primer_dia_semana:
        print("", end="\t")
        contador_columna += 1
 
    
    dia = 1
    while dia <= dias_mes:
        
        print(dia, end="\t")
        contador_columna += 1
 
        
        if contador_columna == 7:
            print()
            contador_columna = 0
 
        dia += 1
 
    
    print()
 
 
main()