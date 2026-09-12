def _cargar_ingresos () -> list[int]:
    """
    Contrato: Carga los números de socios que ingresaron an club, la carga termina cuando se ingresa 0
    
    Precondicion: el número de socio debe ser un número entero

    Postcondicion: Devuelve una lista con los numeros de socio en orden que ingresaron
    
    """

    ingresos = []

    numero_socio = int(input("Ingrese el número de socio (0 para terminar): "))

    while numero_socio != 0:
        ingresos.append(numero_socio)
        numero_socio = int(input("Ingrese el número de socio (0 para terminar): "))

    return ingresos


def _obtener_unicos(lista:list[int]) -> list[int]:
    """
    Contrato: Genera una lista con la lista unica de socios ingresados sin repetir

    Precondicion: lista debe contener enteros

    Postcondicion: Devuelve una lista con los socios ingresados sin repetir    
    
    """

    lista_unicos = []

    for elemento in lista:
        if elemento not in lista_unicos:
            lista_unicos.append(elemento)

    return lista_unicos


def _eliminar_socio(ingresos: list[int], numero_socio: int) -> int:
    """
    Contrato: Elimina todos los ingresos de un socio de la lista e informa cuantos ingresos se eliminaron
    
    Precondiciones: ingresos debe contener enteros

    Postcondiciones: La lista ingresos queda modificada sin ingresos del socio solicitado y devuelve la cantidad de ingresos eliminados
    
    """

    cantidad_eliminados = ingresos.count(numero_socio)

    while numero_socio in ingresos:
        ingresos.remove(numero_socio)

    return cantidad_eliminados


def main() -> None:
    """
    Contrato: Ejecuta el programa principal, registra ingresos, informa cuantas veces ingreso cada socio y permite dar de baja socios
    
    Precondiciones: El archivo debe ejecutarse como programa principal

    Postcondiciones: Muestra el informa de ingresos y el resultado de la baja

    """

    print("Registro de ingresos al club")

    print("Carga de ingresos: ")

    ingresos = _cargar_ingresos()

    print("Informe de ingresos por socio")

    socios_unicos = _obtener_unicos(ingresos)

    for socio in socios_unicos:
        cantidad = ingresos.count(socio)
        print(f"El socio {socio} ingreso {cantidad} veces")

    print("Baja de un socio")
    print("Registro de entradas antes de la baja:")
    print(ingresos)

    socio_a_eliminar = int(input("Ingrese el número de socio a dar de baja: "))
    cantidad_eliminados = _eliminar_socio(ingresos,socio_a_eliminar)

    print("Registro de entradas despues de la baja")
    print(ingresos)
    print(f"Se eliminaron {cantidad_eliminados} ingresos del socio {socio_a_eliminar}")

main()