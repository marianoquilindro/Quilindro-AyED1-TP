import random as rn

def _cargar_lista (n: int) -> list:
    """
    Contrato: Carga una lista de n numeros aleatorios entre 1 y 100

    Precondiciones: n debe ser un entero positivo y se debe importar la libreria random para el uso de la función

    Postcondicion: Devuelve una lista de n enteros entre 1 y 100
    
    """
    lista = []

    contador = 0
    while contador < n:
        valor = rn.randint(1,100)
        lista.append(valor)
        contador += 1

    return lista

def _tiene_repetidos(lista: list) -> bool:
    """
    Contrato: Determina si una lista tiene algun elemento repetido
    
    Precondicion: la lista debe tener enteros

    Postcondicion: Devuelve True si algún elemento aparece mas de una vez o False si no ocurre

    """

    for elemento in lista:
        if lista.count(elemento) > 1:
            return True

    return False

def _obtener_unicos (lista: list) -> list:
    """
    Contrato: Genera una lista nueva con los elementos que no se repiten de la lista original
    
    Precondicion: lista debe tener enteros

    Postcondicion: Devuelve una lista con los elementos que no se repiten en la lista original
    
    """

    lista_unicos = []

    for elemento in lista:
        if elemento not in lista_unicos:
            lista_unicos.append(elemento)

    return lista_unicos


def main() -> None:
    """
    Contrato: Ejecuta el programa principal, genera una lista aleatoria, invoca funciones y muestra los resultados
    
    Precondicion: El archivo debe ejecutarse como programa principal

    Postcondiciones: Muestra la lista generada, si tiene repetidos y la lista con los elementos que no se repiten
    
    """
    print("Generación de lista aleatoria")

    cant_numeros = int(input("Ingrese la cantidad de números que quiere generar: "))

    lista = _cargar_lista(cant_numeros)

    print(f"Lista generada con {len(lista)} elementos")
    print(lista)

    repetidos = _tiene_repetidos(lista)
    print(f"La lista tiene repetidos? {repetidos}")

    unicos = _obtener_unicos(lista)
    print("Lista de elementos que no se repiten")
    print(unicos)

main()