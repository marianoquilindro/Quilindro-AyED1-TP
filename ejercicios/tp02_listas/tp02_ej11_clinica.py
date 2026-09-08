def _cargar_pacientes () -> tuple:
    """
    Contrato: Carga los numeros de afiliado de los pacientes atendidos y los separa en urgencias y turnos, la carse termina cuando el usuario ingresa -1

    Precondicion: El numero de afiliado del paciente debe ser un entero distinto a -1

    Postcondicion: Devuelve una tupla con los numeros de afiliado en el orden que se ingresan y si fue un turno o una urgencia    
    
    """

    urgencias = []
    turnos = []

    numero_afiliado = int(input("Ingrese el numero de afiliado (-1 para terminar): "))

    while numero_afiliado != -1:
        tipo_atencion = int(input("Ingrese 0 si es urgencia o 1 si es un turno: "))

        while tipo_atencion != 0 and tipo_atencion != 1:
            tipo_atencion = int(input("Ingrese 0 si es urgencia o 1 si es un turno: "))

        if tipo_atencion == 0:
            urgencias.append(numero_afiliado)
        else:
            turnos.append(numero_afiliado)

        numero_afiliado = int(input("Ingrese el numero de afiliado (-1 para terminar): "))

    return urgencias, turnos


def _buscar_afiliado (urgencias: list, turnos: list, numero_afiliado: list) -> tuple:
    """
    Contrato: Busca cuantas veces fue atendido un numero de afiliado por urgencias y cuantas por turnos

    Precondicion: urgencias y turnos deben ser listas de enteros y numero afiliado debe ser entero

    Postcondicion: Devuelve una tupla con la cantidad de apariciones del numero de afiliado en urgencias y turnos
    
    """

    veces_urgencia = urgencias.count(numero_afiliado)
    veces_turno = turnos.count(numero_afiliado)

    return veces_urgencia, veces_turno



def main() -> None:
    """
    Contrato: Ejecuta el programa principal, carga los pacientes, muestra las listas por tipo de atencion y permite buscar afiliados

    Precondicion: El archivo debe ejecutarse como programa principal

    Postcondicion: Muestra los listados y los resultados de las busquedas
    
    """

    print("Carga de pacientes")
    urgencias, turnos = _cargar_pacientes()

    print("Pacientes atendidos por urgencia")
    print(urgencias)

    print("Pacientes atendidos por turnos")
    print(turnos)

    print("Busqueda de afiliados")

    afiliado_buscado = int(input("Ingrese el numero de afiliado a buscar (-1 para salir): "))
    while afiliado_buscado != -1:
        veces_urgencia, veces_turno = _buscar_afiliado(urgencias,turnos,afiliado_buscado)
        print(f"El afiliado {afiliado_buscado} fue atentido {veces_turno} veces por turno y {veces_urgencia} veces por urgencia")
        afiliado_buscado = int(input("Ingrese el numero de afiliado a buscar (-1 para salir): "))


main()    