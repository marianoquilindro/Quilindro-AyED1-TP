def main() -> None:
    """
    Contrato: Ejecuta el programa principal, crea una lista por comprension con los naipes de la baraja española

    Precondición: El archivo debe ejecutarse como programa principal

    Postcondición: Muestara la lisa de naipes y la cantidad de cartas
    """

    print("Naipes de la baraja española")

    palos = ["Oro", "Copa", "Espada", "Basto"]
    numeros = [num for num in range(1,13)]

    naipes = [f"{numero} {palo}" for palo in palos for numero in numeros]

    print(naipes)
    print(f"Cantidad de cartas: {len(naipes)}")

main()