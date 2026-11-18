import random as rn

PISOS = 10
HABITACIONES_POR_PISO = 6
CAPACIDAD = PISOS * HABITACIONES_POR_PISO


def _esbisiesto(anio: int) -> bool:
    """
    Contrato: Determina si un año es bisiesto

    Precondiciones: anio debe ser un entero positivo

    Postcondiciones: Devuelve True si el año es bisiesto y False si no lo es

    """
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)


def _dias_del_mes(mes: int, anio: int) -> int:
    """
    Contrato: Devuelve la cantidad de días que tiene un mes de un año, teniendo en cuenta los años bisiestos

    Precondición: mes debe ser un número entero entre 1 y 12 y anio un número entero mayor o igual a 1

    Postcondición: Devuelve la cantidad de días del mes
    """
    dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    dias = dias_por_mes[mes - 1]

    if mes == 2 and _esbisiesto(anio):
        dias = 29

    return dias


def _separar_fecha(fecha: str) -> tuple:
    """
    Contrato: Separa una fecha en formato DDMMAAAA en números

    Precondición: fecha debe ser una cadena de 8 digitos

    Postcondición: Devuelve una tupla (dia, mes, año) de números enteros
    """
    return (int(fecha[0:2]), int(fecha[2:4]), int(fecha[4:8]))


def _fecha_valida(fecha: str) -> bool:
    """
    Contrato: Verifica que una cadena sea una fecha válida del calendario

    Precondición: fecha debe ser una cadena de texto

    Postcondición: Devuelve True si la cadena tiene 8 dígitos y representa una fecha existente, False si no lo es
    """
    valida = False

    if len(fecha) == 8 and fecha.isdigit():
        dia, mes, anio = _separar_fecha(fecha)

        if anio >= 1 and 1 <= mes <= 12:
            valida = 1 <= dia <= _dias_del_mes(mes, anio)

    return valida


def _fecha_a_numero(fecha: str) -> int:
    """
    Contrato: Convierte una fecha DDMMAAAA en número AAAAMMDD

    Precondición: fecha debe ser una fecha válida en formato DDMMAAAA

    Postcondición: Devuelve un número entero con el formato AAAAMMDD
    """
    dia, mes, anio = _separar_fecha(fecha)

    return anio * 10000 + mes * 100 + dia


def _dias_entre(ingreso: str, egreso: str) -> int:
    """
    Contrato: Calcula la cantidad de días entre dos fechas

    Precondición: ingreso y egreso deben ser fechas válidas en formato DDMMAAAA

    Postcondición: Devuelve la cantidad de días entre abas fechas (0 si el egreso no es posterios al ingreso)
    """
    dia, mes, anio = _separar_fecha(ingreso)
    limite = _fecha_a_numero(egreso)
    dias = 0

    while anio * 10000 + mes * 100 + dia < limite:
        dia += 1

        if dia > _dias_del_mes(mes, anio):
            dia = 1
            mes += 1

            if mes > 12:
                mes = 1
                anio += 1

        dias += 1

    return dias


def _formatear_fecha(fecha: str) -> str:
    """
    Contrato: Convierte una fecha en formato DDMMAAAA a formato DD/MM/AAAA

    Precondición: fecha debe ser una fecha válida en formato DDMMAAAA

    Postcondición: Devuelve la fecha con barras separadoras
    """
    return fecha[0:2] + "/" + fecha[2:4] + "/" + fecha[4:8]


def _leer_dni(dnis_registrados: list) -> int:
    """
    Contrato: Pide un número de dni hasta que sea válido

    Precondición: dnis_registrados debe ser una lista de dnis ya registrados

    Postcondición: Devuelve un dni válido no repetido o -1 si el usuario termina
    """
    dni = 0
    valido = False

    while not valido:
        entrada = input("DNI del cliente (-1 para terminar): ").strip()

        try:
            dni = int(entrada)

            if dni == -1:
                valido = True
            elif dni <= 0:
                print("El DNI debe ser un número entero positivo")
            elif dni in dnis_registrados:
                print("Ese DNI ya fue registrado")
            else:
                valido = True
        except ValueError:
            print("Debe ingresar un número entero")

    return dni


def _leer_nombre() -> str:
    """
    Contrato: Pide el apellido y nombre del cliente hasta que no este vacío y no tenga comas

    Precondición: -

    Postcondición: Devuelve el apellido y nombre ingresado
    """
    nombre = input("Apellido y nombre (sin comas): ").strip()

    while nombre == "" or "," in nombre:
        print("El nombre no puede estar vacío ni tener comas")
        nombre = input("Apellido y nombre (sin comas): ").strip()

    return nombre


def _leer_fecha(mensaje: str) -> str:
    """
    Contrato: Pide una fecha en formato DDMMAAAA hasta que sea una fecha válida

    Precondición: mensaje debe ser la cadena que se muestra al pedir la fecha

    Postcondición: Devuelve la fecha ingresada como cadena
    """
    fecha = input(mensaje).strip()

    while not _fecha_valida(fecha):
        print("Fecha inválida. Usar el formato DDMMAAAA")
        fecha = input(mensaje).strip()

    return fecha


def _leer_ocupantes() -> int:
    """
    Contrato: Pide la cantidad de ocupantes hasta que sea un número entero mayor o igual a 1

    Precondición: -

    Postcondición: Devuelve la cantidad de ocupantes ingresada
    """
    ocupantes = 0

    while ocupantes < 1:
        try:
            ocupantes = int(input("Cantidad de ocupantes: ").strip())

            if ocupantes < 1:
                print("Debe haber al menos un ocupante")
        except ValueError:
            print("Debe ingresar un número entero")

    return ocupantes


def _registrar_huespedes(nombre_archivo: str) -> int:
    """
    Contrato: Registra el ingreso de huespedes hasta que se ingresa -1 en el DNI o hasta completar la capacidad del hotel. Guarda los registros en un archivo csv y verifica que los dni no se repitan

    Precondición: nombre_archivo debe ser una cadena de texto con el nombre del archivo csv a generar

    Postcondición: Crea o sobrescribe el archivo csv con el registro de huespedes y devuelve la cantidad de registros grabados
    """
    dnis = []

    try:
        with open(nombre_archivo, "wt", encoding="utf-8") as archivo:
            dni = _leer_dni(dnis)

            while dni != -1 and len(dnis) < CAPACIDAD:
                nombre = _leer_nombre()
                ingreso = _leer_fecha("Fecha de ingreso (DDMMAAAA): ")
                egreso = _leer_fecha("Fecha de egreso (DDMMAAAA): ")

                while _fecha_a_numero(egreso) <= _fecha_a_numero(ingreso):
                    print("La fecha de egreso tiene que ser posterior a la de ingreso")
                    egreso = _leer_fecha("Fecha de egreso (DDMMAAAA): ")

                ocupantes = _leer_ocupantes()

                archivo.write(
                    ",".join([str(dni), nombre, ingreso, egreso, str(ocupantes)]) + "\n"
                )

                dnis.append(dni)

                if len(dnis) == CAPACIDAD:
                    print(
                        f"El hotel completo sus {CAPACIDAD} habitaciones. No se admiten mas registros"
                    )
                else:
                    dni = _leer_dni(dnis)
    except FileNotFoundError:
        print(f"Error: no se pudo crear el archivo {nombre_archivo}")

    return len(dnis)


def _habitacion_libre(huespedes: list, piso: int, habitacion: int) -> bool:
    """
    Contrato: Verifica si una habitación todavía no fue asignada a ningun huesped

    Precondición: huespedes debe ser una lista de registros [dni, nombre, ingreso, egreso, ocupantes, piso, habitacion]

    Postcondición: Devuelve True si ningun huesped tiene asignado ese piso y esa habitación, False en caso contrario
    """
    libre = True

    for huesped in huespedes:
        if huesped[5] == piso and huesped[6] == habitacion:
            libre = False

    return libre


def _elegir_habitacion(huespedes: list) -> tuple:
    """
    Contrato: Elige un piso y una habitacion al azar en la que no hayan asignado huespedes todavia

    Precondición: huespedes debe ser una lista de registros con menos huespedes que la capacidad del hotel

    Postcondición: Devuelve una tupla (piso, habitacion) correspondiente a una habitación libre
    """
    piso = rn.randint(1, PISOS)
    habitacion = rn.randint(1, HABITACIONES_POR_PISO)

    while not _habitacion_libre(huespedes, piso, habitacion):
        piso = rn.randint(1, PISOS)
        habitacion = rn.randint(1, HABITACIONES_POR_PISO)

    return (piso, habitacion)


def _asignar_habitaciones(nombre_archivo: str) -> list:
    """
    Contrato: Lee el archivo csv de huespedes y asigna a cada uno un piso y una habitacion elegidos al azar, sin repetir una habitación ocupada

    Precondición: nombre_archivo debe ser el archivo csv generadp por _registrar_huespedes

    Postcondición: Devuelve una lista de registros [din, nombre, ingreso, egreso, ocupantes, piso, habitacion], los registros inválidos se omiten
    """
    huespedes = []

    try:
        with open(nombre_archivo, "rt", encoding="utf-8-sig") as archivo:
            linea = archivo.readline()

            while linea != "":
                linea = linea.rstrip("\n")

                if linea.strip() != "":
                    campos = linea.split(",")

                    if len(campos) != 5:
                        print(f"Registro inválido se omite: {linea}")
                    else:
                        try:
                            dni = int(campos[0])
                            nombre = campos[1]
                            ingreso = campos[2]
                            egreso = campos[3]
                            ocupantes = int(campos[4])

                            if not _fecha_valida(ingreso) or not _fecha_valida(egreso):
                                print(f"Registro invalido se omite: {linea}")
                            elif len(huespedes) >= CAPACIDAD:
                                print(f"No hay habitaciones libres para {nombre}")
                            else:
                                piso, habitacion = _elegir_habitacion(huespedes)
                                huespedes.append(
                                    [
                                        dni,
                                        nombre,
                                        ingreso,
                                        egreso,
                                        ocupantes,
                                        piso,
                                        habitacion,
                                    ]
                                )

                        except ValueError:
                            print(f"Registro invalido se omite: {linea}")

                linea = archivo.readline()
    except FileNotFoundError:
        print(f"Error: el archivo {nombre_archivo} no existe")

    return huespedes


def _mostrar_asignaciones(huespedes: list) -> None:
    """
    Contrato: Muestra la habitación asignada a cada huesped

    Precondición: huespedes debe ser una lista de registros [dni, nombre, ingreso, egreso, ocupantes, piso, habitacion]

    Postcondición: Muestra una linea por huesped con su piso y habitación
    """
    for dni, nombre, ingreso, egreso, ocupantes, piso, habitacion in huespedes:
        print(f"Piso {piso} habitación {habitacion} : {nombre}")


def _mostrar_pisos_maximos(totales: list, unidad: str) -> None:
    """
    Contrato: Muestra el piso o los pisos con el mayor valor de una lista de totales por piso

    Precondición: totales debe ser una lista con un total por cada piso y unidad una cadena que describe lo que se cuenta

    Postcondición: Muestra el piso o los pisos con el máximo y su cantidad
    """
    maximo = max(totales)

    for i in range(PISOS):
        if totales[i] == maximo:
            print(f"Piso {i + 1} con {maximo} {unidad}")


def _mostrar_piso_mas_ocupado(huespedes: list) -> None:
    """
    Contrato: Muestra el piso con mayor de cantidad de habitaciones ocupadas

    Precondición: huespedes debe ser una lista de registro con al menos un elemento

    Postcondición: Muestra el o los pisos con más habitaciones ocupadas
    """
    habitaciones_por_piso = [0] * PISOS

    for dni, nombre, ingreso, egreso, ocupantes, piso, habitacion in huespedes:
        habitaciones_por_piso[piso - 1] += 1

    _mostrar_pisos_maximos(habitaciones_por_piso, "habitaciones ocupadas")


def _mostrar_piso_mas_personas(huespedes: list) -> None:
    """
    Contrato: Muestra el piso con mayor cantidad de personas, sumando los ocupantes de cada habitación

    Precondición: huespedes debe ser una lista de registros con al menos un elemento

    Postcondición: Muestra el o los pisos con más personas
    """
    personas_por_piso = [0] * PISOS

    for dni, nombre, ingreso, egreso, ocupantes, piso, habitacion in huespedes:
        personas_por_piso[piso - 1] += ocupantes
    _mostrar_pisos_maximos(personas_por_piso, "personas")


def _mostrar_habitaciones_vacias(huespedes: list) -> None:
    """
    Contrato: Muestra cuantas habitaciones vacías hay en todo el hotel

    Precondición: huespedes debe ser una lista de registros con habitación asignada

    Postcondición: Muestra la cantidad de habitaciones vacías
    """
    vacias = CAPACIDAD - len(huespedes)

    print(f"Habitaciones vacías en el hotel: {vacias} de {CAPACIDAD}")


def _mostrar_proxima_a_desocuparse(huespedes: list, fecha_actual: str) -> None:
    """
    Contrato: Muestra la proxima habitación a desocuparse, que es la que tiene fecha de egreso más cercana

    Precondición: huespedes debe ser una lista de registros y fecha actual una fecha válida

    Postcondición: Muestra la o las habitaciones proximas a desocuparse o un aviso si todas las fechas de egreso ya pasaron
    """
    actual = _fecha_a_numero(fecha_actual)
    proxima = ""

    for dni, nombre, ingreso, egreso, ocupantes, piso, habitacion in huespedes:
        if _fecha_a_numero(egreso) >= actual:
            if proxima == "" or _fecha_a_numero(egreso) < _fecha_a_numero(proxima):
                proxima = egreso

    if proxima == "":
        print(
            "No hay habitaciones por desocuparse, todas las fechas de egreso ya pasaron"
        )
    else:
        print(f"Proxima fecha de egreso {_formatear_fecha(proxima)}")

        for dni, nombre, ingreso, egreso, ocupantes, piso, habitacion in huespedes:
            if egreso == proxima:
                print(f"Piso {piso} habitación {habitacion} {nombre}")


def _mostrar_listado_por_estadia(huespedes: list) -> None:
    """
    Contrato: Muestra un listado de todos los huespedes ordenado por cantidad de días de alojamiento de menor a mayor

    Precondición: huespedes debe ser una lista de registros

    Postcondición: Muestra cada huesped con sus días de alojamiento y su habitación
    """
    listado = []

    for dni, nombre, ingreso, egreso, ocupantes, piso, habitacion in huespedes:
        dias = _dias_entre(ingreso, egreso)
        listado.append([dias, nombre, dni, piso, habitacion])

    listado.sort()

    for dias, nombre, dni, piso, habitacion in listado:
        print(f"{nombre} DNI {dni} dias {dias} piso {piso} habitación {habitacion}")


def main() -> None:
    """
    Contrato: Ejecuta el programa principal, registra huespedes en un archivo csv, les asigna una habitación y muestra información sobre el ocupante

    Precondición: El archivo debe ejecutarse como programa principal

    Postcondición: Genera huespedes.csv y muestra los resultados de las consultas
    """
    print("Gestión de habitaciones de hotel")

    _registrar_huespedes("huespedes.csv")
    huespedes = _asignar_habitaciones("huespedes.csv")

    if len(huespedes) == 0:
        print("No hay huespedes registrados")
    else:
        fecha_actual = _leer_fecha("Ingrese la fecha actual (DDMMAAAA): ")

        print("Habitaciones asignadas:")
        _mostrar_asignaciones(huespedes)

        print("Piso con mayor cantidad de habitaciones ocupadas:")
        _mostrar_piso_mas_ocupado(huespedes)

        _mostrar_habitaciones_vacias(huespedes)

        print("Piso con mayor cantidad de personas: ")
        _mostrar_piso_mas_personas(huespedes)

        print("Próxima habitación en desocuparse:")
        _mostrar_proxima_a_desocuparse(huespedes, fecha_actual)

        print("Huespedes ordenados por días de alojamiento de menor a mayor:")
        _mostrar_listado_por_estadia(huespedes)


main()
