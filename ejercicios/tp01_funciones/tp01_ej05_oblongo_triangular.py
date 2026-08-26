_es_oblongo = lambda n: any(k*(k+1) == n for k in range (0, n+1))

_es_triangular = lambda n: any(k*(k+1) // 2 == n  for k in range (1, n+1))


def main()-> None:
    """
    Contrato: Ejecuta el programa principal, pide un numero al usuario y verifica si es oblongo y si es triangular

    Precondiciones: El archivo debe ejecutarse como programa principal
    
    Postcondiciones: Muestra si el numero ingresado es oblongo o si es triangular
    """

    print("Verificación de números oblongos y triangulares")

    numero = int(input("Ingrese un número: "))

    print(f"¿El número {numero} es oblongo?  {_es_oblongo(numero)}")
    print(f"¿El número {numero} es triangular?  {_es_triangular(numero)}")


main()