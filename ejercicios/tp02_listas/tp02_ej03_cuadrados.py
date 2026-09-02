def _generar_cuadrados(n: int) -> list:
    """
    Contrato: Crea una lista con los cuadrados de los numeros entre 1 y n
    
    Precondicion: n debe ser un entero positivo

    Postcondicion: Devuelve una lista con los cuadrados de 1 a n
    
    """

    lista = []

    numero = 1
    while numero <= n:
        lista.append(numero ** 2)
        numero += 1

    return lista

def _guardar_ultimos_diez (lista: list) -> list:
    """
    Contrato: Imprime los ultimos 10 elementos de una lista, si tiene menos de 10 elementos muestra todos
    
    Precondiciones: lista debe tener enteros
    
    Postcondiciones: Muestra los elementos correspondientes

    """

    if len(lista) >= 10:
        indice_inicio = len(lista) - 10
    else:
        indice_inicio = 0


    ultimos_diez = []


    indice = indice_inicio
    while indice < len(lista):
        ultimos_diez.append(lista[indice])
        indice += 1

    return ultimos_diez

def main() -> None:
    """
    Contrato: Ejecuta el programa principal, solicita un numero al usuario que es el limite de la lista y muestra los ultimos 10 cuadrados de la lista

    Precondicion: El archivo debe ejecutarse como programa principal
    
    Postcondicion: Muestra los ultimos 10 valores de la lista de cuadrados
    
    """

    print("Lista de cuadrados")

    limite = int(input("Ingrese el limite: "))
    lista = _generar_cuadrados(limite)
    print(lista)

    ultimos_diez = _guardar_ultimos_diez(lista)
    print("Ultimos 10")
    print(ultimos_diez)


main()