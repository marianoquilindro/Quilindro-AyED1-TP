def main() -> None:
    """
    Contrato: Ejecuta el programa principal, solicita al usuario dos numeros y muestra los multiplos de 7 que no son multiplos de 5 entre los valores ingresados

    Precondicion: El archivo debe ejecutarse como programa principal

    Postcondicion: Muestra la lista generada
    
    """

    a = int(input("Ingrese el valor de A: "))
    b = int(input("Ingrese el valor de B: "))

    print("Multiplos de 7 que no son multiplos de 5")

    lista = [numero for numero in range (a,b + 1) if numero % 7 == 0 and numero %5]

    print(lista)

main()