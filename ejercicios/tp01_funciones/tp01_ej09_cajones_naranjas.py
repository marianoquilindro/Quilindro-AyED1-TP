import random as rn

def _generar_pesos(cantidad: int) -> list[int]:
    """
    Contrato: Genera una lista con el peso generado de manera aleatoria en gramos de cada naranja
    
    Precondicion: cantidad debe ser un entero positivo

    Postcondicion: Devuelve una lista de enteros entre 150 y 350, uno por cada naranja
    
    """

    pesos = []
    contador = 0

    while contador < cantidad:
        peso = rn.randint(150,350)
        pesos.append(peso)
        contador += 1

    return pesos

def _clasificar_naranjas (pesos: list[int]) -> tuple[int, int, int, int]:
    """
    Contrato: Clasifica las naranjas en cajones completos (de 100 naranjas aptas cada uno), sobrante para el próximo reparto y naranja para jugo, acumula el peso de las naranjas que si se despachan en cajones llenos
    
    Precondicion: pesos debe ser una lista de enteros positivos
    
    Postcondicion: Devuelve una tupla correspondiente a cajones llenos, sobrante, juego y peso despachado en gramos

    """

    aptas_en_cajon_actual = 0
    peso_cajon_actual = 0
    cajones_llenos = 0
    peso_despachado = 0
    jugo = 0

    indice = 0
    while indice < len(pesos):
        peso = pesos[indice]

        if peso >= 200 and peso <= 300:
            aptas_en_cajon_actual += 1
            peso_cajon_actual += peso

            if aptas_en_cajon_actual == 100:
                cajones_llenos += 1
                peso_despachado += peso_cajon_actual
                aptas_en_cajon_actual = 0
                peso_cajon_actual = 0
        else: 
            jugo += 1

        indice += 1
    sobrante = aptas_en_cajon_actual

    return cajones_llenos, sobrante, jugo, peso_despachado


def _calcular_camiones(peso_despachado: int) -> int:
    """
    Contrato: Calcula la cantidad de camiones necesarios para transportar el peso despachado, considerando que un camión no se despacha si no se ocupa el 80% de su capacidad
    
    Precondicion: peso_despachado debe ser un entero positivo 0 cero que represente una medida en gramos
    
    Postcondicion: Devuelve la cantidad de camiones necesarios para despachar esa cantidad de peso

    """

    capacidad_camion = 500000

    camiones_completos = peso_despachado // capacidad_camion
    resto = peso_despachado % capacidad_camion

    if resto == 0:
        cantidad_camiones = camiones_completos
    else: 
        ocupacion = resto / capacidad_camion
        if ocupacion >= 0.8:
            cantidad_camiones = camiones_completos + 1
        else:
            cantidad_camiones = camiones_completos

    return cantidad_camiones

def main() -> None:
    """
    Contrato: Ejecuta el programa principal, solicita una cantidad de naranjas y muestra la cantidad de cajones, lo que sobra, las naranjas que se usan para jugo y los camiones necesarios para transportarlas
    
    Precondicion: El archivo debe ejecutarse como programa principal

    Postcondiciones: Muestra el resultado de la clasificación y el calculo de los camiones necesarios
    
    """

    print("Cuenta de cajones de naranjas")

    cantidad_naranjas = int(input("Ingrese la cantidad de naranjas cosechadas: "))

    pesos = _generar_pesos(cantidad_naranjas)
    cajones_llenos, sobrante, jugo, peso_despachado = _clasificar_naranjas(pesos)
    cantidad_camiones = _calcular_camiones(peso_despachado)

    print(f"Cajones que se pueden llenar: {cajones_llenos}")
    print(f"Naranjas sobrantes: {sobrante}")
    print(f"Naranjas para jugo: {jugo}")
    print(f"Peso total despachado: {peso_despachado} gramos")
    print(f"camiones necesarios: {cantidad_camiones}")

main()