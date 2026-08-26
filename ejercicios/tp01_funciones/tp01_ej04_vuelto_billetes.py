def _calcular_billetes(vuelto: int) -> tuple[list[int], int]:
    """
    Contrato: Calcula cuántos billetes de cada denominación entran en el vuelto, comenzado por el billete mas grande

    Precondicion: vuelto debe ser un entero mayor o igual a 0
    
    Postcondicion: Devuelve una lista con la cantidad de billetes de cada denominacion (en el mismo orden que las denominaciones) y el resto que no pudo cubrir con ningun billete
    """

    denominaciones = [5000, 1000, 500, 200, 100, 50, 10]
    cantidad_billetes = []
    vuelto_restante = vuelto

    for billete in denominaciones:
        cantidad = vuelto_restante // billete
        vuelto_restante = vuelto_restante % billete
        cantidad_billetes.append(cantidad)

    return cantidad_billetes, vuelto_restante


def main() -> None:
    """
    Contrato: Ejecuta el programa principal solicitando el total de la compra y el dinero recibido, muestra la cantidad de billetes a entregar como vuelto
    
    Precondiciones: El archivo debe ejecutarse como programa principal
    
    Postcondiciones: Muestra el detalle del vuelto o mensaje de error
    """

    denominaciones = [5000, 1000, 500, 200, 100, 50, 10]

    print("Cálculo de vuelto")

    total_compra = int(input("Ingrese el total de la compra: "))
    dinero_recibido = int(input("Ingrese el dinero recibido: "))

    if dinero_recibido < total_compra:
        print("Error: el dinero recibido es insuficiente")
        return

    vuelto = dinero_recibido - total_compra

    cantidad_billetes, resto = _calcular_billetes(vuelto)

    if resto != 0:
        print("Error no se puede entregar el vuelto exacto con las denominaciones disponibles")
        return

    print(f"El vuelto a entregar es de ${vuelto}:")

    for i, element in enumerate (denominaciones):
        if cantidad_billetes[i] > 0:
            print(f"{cantidad_billetes[i]} billete/s de ${element}")



main()


