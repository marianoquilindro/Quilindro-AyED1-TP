def main() -> None:
    """
    Contrato: Ejecuta el programa principal, construye y muestra una lista de números impares entre 100 y 200

    Precondicion: El archivo debe ejecutarse como programa principal

    Postcondicion: Muestra la lista de impares generada
    
    """

    print("Números impares entre 100 y 200")

    impares =  [numero for numero in range(100,201) if numero %2]

    print(impares)

main()