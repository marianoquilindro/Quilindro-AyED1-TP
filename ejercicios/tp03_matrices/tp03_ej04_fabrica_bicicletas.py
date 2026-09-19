import random as rn

def _imprimir_matriz(matriz: list[list[int]]) -> None:
    """
    Contrato: Imprime la matriz, mostrando cada fila en una linea distinta

    Precondicion: matriz debe ser una lista de lista de enteros

    Postcondicion: Muestra el contenido de la matriz

    """

    fila = 0
    while fila < len(matriz):
        print(matriz[fila])
        fila += 1

def _generar_produccion(n: int) -> list[list[int]]:
    """
    Contrato: Genera una matriz con la producción diaria de bicicletas de una n cantidad de fabricas durante seis días (de lunes a sábados) con números al azar entre 0 y 150

    Precondiciones: n debe ser un entero positivo

    Postcondiciones: Devuelve una matriz con n cantidad de filas y 6 columnas con valores al azar entre 0 y 150
    
    """

    dias_semana = 6
    matriz = []

    fabrica = 0

    while fabrica < n:
        fila = []

        dia = 0
        while dia < dias_semana:
            produccion = rn.randint(0, 150)
            fila.append(produccion)
            dia += 1

        matriz.append(fila)
        fabrica += 1

    return matriz


def _total_por_fabrica(matriz: list[list[int]]) -> list[int]:
    """
    Contrato: Calcula el total de bicicletas producidas por cada fabrica durante los seis días

    Precondicion: matriz debe ser una lista de lista de enteros
    
    Postcondicion: Devuelve una lista con el total de cada fabrica, respetando el orden de las filas de la matriz

    """

    totales = []

    fabrica = 0
    while fabrica < len(matriz):
        total = sum(matriz[fabrica])
        totales.append(total)
        fabrica += 1

    return totales


def _fabrica_mas_productiva(matriz: list[list[int]]) -> tuple[int, int, int]:
    """
    Contrato: Determina cual es la fábrica que más produjo en un solo dá, indica cual es la fábrica, el día y la cantidad producida

    Precondicion: matriz debe ser una lista de enteros no vacía

    Postcondicion: Devuelve una tupla con la posicion de la fábrica, el día que mas se produjo y el valor de ese día
    
    """
    maximo = matriz[0][0]
    fabrica_productiva = 0
    dia_productivo = 0

    fabrica = 0
    while fabrica < len(matriz):
        dia = 0

        while dia < len(matriz[fabrica]):
            if matriz[fabrica][dia] > maximo:
                maximo = matriz[fabrica][dia]
                fabrica_productiva = fabrica
                dia_productivo = dia
            dia += 1

        fabrica += 1

    return fabrica_productiva, dia_productivo, maximo


def _dia_mas_productivo(matriz: list[list[int]]) -> tuple[int, int]:
    """
    Contrato: Determina cuál es el día más productivo teniendo en cuenta todas las fábricas

    Precondicion: matriz debe ser una lista de enteros no vacía y con todas las filas del mismo largo
    
    Postcondicion: Devuelve una tupla con el día de mayor producción y el valor de ese día

    """

    cantidad_dias = (len(matriz[0]))
    totales_dia = []

    dia = 0
    while dia < cantidad_dias:
        suma_dia = 0

        fabrica = 0
        while fabrica < len(matriz):
            suma_dia += matriz[fabrica][dia]
            fabrica += 1

        totales_dia.append(suma_dia)
        dia += 1

    dia_maximo = 0
    maximo = totales_dia[0]

    dia = 1
    while dia < len(totales_dia):
        if totales_dia[dia] > maximo:
            maximo = totales_dia[dia]
            dia_maximo = dia
        dia += 1

    return dia_maximo, maximo





def main() -> None:
    """
    Contrato: Ejecuta el programa principal, solicita un número n y genera la matriz correspondiente a las fabricas y la produccion
    
    Precondicion: El archivo debe ejecutarse como programa principal

    Postcondicion: Muestra la matriz generada y los distintos resultados
    
    """

    dias = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado")

    print("Producción semanal de bicicletas por fábrica")

    n = int(input("ingrese la cantidad de fabricas: "))
    matriz = _generar_produccion(n)

    print("Matriz de producción (filas: fábricas, columnas: lunes a sábado): ")
    _imprimir_matriz(matriz)


    print("Total producido por cada fábrica")
    totales = _total_por_fabrica(matriz)
    print(totales)

    fabrica_maxima, dia_maximo, cantidad_maxima = _fabrica_mas_productiva(matriz)
    print(f"La fábrica que más produjo en un día fue la fábrica {fabrica_maxima + 1}, una cantidad de {cantidad_maxima} el día {dias[dia_maximo]}")


    dia_top, total_dia_top = _dia_mas_productivo(matriz)
    print(f"El día mas productivo teniendo en cuenta todas las fábricas fue el dia {dias[dia_top]} que se hicieron {total_dia_top} bicicletas")


    minimos = [min(fila) for fila in matriz]
    print(f"Menor cantidad fabricada por cada fábrica: {minimos}")

main()
