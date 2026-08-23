def _calcular_gasto_subte (cantidad_viajes: int) -> float:
    """
    Contrato: Calcula el gasto toal en viajes en subte durante un mes, utilizando un esquema de tarifas decrecientes segun la cantidad de viajes realizados

    Precondiciones: cantidad_viajes debe ser un entero positivo

    Postcondiciones: Devuelve el gasto total como numero    
    """

    tarifa_maxima = 1684.0

    if cantidad_viajes <= 20:
        tramo1 = cantidad_viajes
        tramo2 = 0
        tramo3 = 0
        tramo4 = 0
    elif cantidad_viajes <= 30:
          tramo1 = 20
          tramo2 = cantidad_viajes -20
          tramo3 = 0
          tramo4 = 0
    elif cantidad_viajes <= 40:
          tramo1 = 20
          tramo2 = 10
          tramo3 = cantidad_viajes -30
          tramo4 = 0
    else:
         tramo1 = 20
         tramo2 = 10
         tramo3 = 10
         tramo4 = cantidad_viajes -40

    total = (tramo1 * tarifa_maxima + tramo2 * tarifa_maxima *0.80 + tramo3 * tarifa_maxima * 0.70 + tramo4 * tarifa_maxima * 0.60)

    return total

def main () -> None:
     """
     Contrato: Ejecuta el programa principal, solicita cantidad de viajes realizados en el mes y muestra el gasto total

     Precondiciones: El archivo debe ejecutarse como programa principal

     Postcondiciones: Muestra por pantalla el gasto calculado
     """

     print("Cálculo mensual de gasto en subte")

     cantidad_viajes = int(input("Ingrese la cantidad de viajes realizados en el mes: "))

     gasto_total = _calcular_gasto_subte(cantidad_viajes)

     print(f"El gasto total en subte fue de ${gasto_total:.2f}")


main()