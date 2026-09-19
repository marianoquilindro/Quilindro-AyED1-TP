import random as rn

def _cargar_sala(n: int, m: int) -> list[list[int]]:
    """
    Contrato: Carga con n cantidad de filas por m cantidad de butacas con valores al azar entre 0 y 1, siendo 0 libre y 1 reservada

    Postcondición: n y m deben ser entero positivos

    Precondición: Devuelve una matrid de N x M con valores al azar entre 0 y 1
    
    """

    sala = []

    fila = 0
    while fila < n:
        fila_actual = []

        columna = 0
        while columna < m:
            estado = rn.randint(0, 1)
            fila_actual.append(estado)
            columna += 1

        sala.append(fila_actual)
        fila += 1

    return sala


def _mostrar_butacas(sala: list[list[int]]) -> None:
    """
    Contrato: Muestra el estado de cada una de las butacas de la sala, indicando si esta libre o reservada

    Precondición: sala debe ser una matriz de enteros con valores 0 o 1

    Postcondición: Muestra el estado de cada butaca
    
    """
    fila = 0
    while fila < len(sala):
        print(f"Fila {fila +1}")
        columna = 0
        while columna < len(sala[fila]):
            valor = sala[fila][columna]

            if valor == 1:
                print("Reservada")
            else:
                print("Libre")

            columna += 1

        fila += 1


def _reservar(sala: list[list[int]], fila: int, columna: int) -> bool:
    """
    Contrato: Reserva una butaca si se encuentra disponible

    Precondición: fila y columna deben ser índices válidos de la sala

    Postcondición: Si la butaca está libre la reserva y devuelve True, en el caso que ya este reservada devuelve False
    
    """

    if sala[fila][columna] == 0:
        sala[fila][columna] = 1
        return True
    else:
        return False



def _butacas_libres (sala: list[list[int]]) -> int:
    """
    Contrato: Cuenta la cantidad de butacas desocupadas que hay en la sala

    Precondición: sala debe ser una matriz de enteros con valores 0 y 1

    Postcondición: Devuelve la cantidad total de butacas disponibles en la sala    
    
    """

    total_libres = 0

    fila = 0
    while fila < len(sala):
        total_libres += sala[fila].count(0)
        fila += 1

    return total_libres







def main():
    """
    
    
    """
    print("Sala de cine")

    n = int(input("Ingrese la cantidad de filas: "))
    m = int(input("Ingrese la cantidad de butacas: "))

    sala = _cargar_sala(n, m)

    print("Estado de la sala:")
    _mostrar_butacas(sala)


    fila_reserva = int(input("Ingrese la fila de la butaca que quiere reservar ( 0 a N-1): "))
    columna_reserva = int(input("Ingrese la columna de la butaca que quiere reservar (0 a M-1): "))

    reserva = _reservar(sala, fila_reserva, columna_reserva)

    if reserva:
        print("Reserva guardada con éxito")
    else:
        print("No se pudo guardar la reserva, la butaca ya esta ocupada")

    _mostrar_butacas(sala)


    lugares_libres = _butacas_libres(sala)
    print(f"cantidad de butacas libres: {lugares_libres}")



main()