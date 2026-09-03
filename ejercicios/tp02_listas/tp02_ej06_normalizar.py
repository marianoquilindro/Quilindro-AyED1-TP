def _normalizar(lista: list) -> list:
    """
    Contrato: Normaliza una lista de numeros enteros, divide los elementos por la suma total de todos los elementos de la lista y los devuelve en una nueva lista

    Precondicion: lista no debe ser vacia y debe contener enteros

    Postcondicion: Devuelve una lista y los resultados de la lista suman 1
    
    """
    suma = sum(lista)

    lista_normalizada = []
    for elemento in lista:
        lista_normalizada.append(elemento / suma)

    return lista_normalizada

def main() -> None:
    """
    Contrato: Ejecuta el programa principal, verifica el comportamiento de la funcion

    Precondicion: El archivo debe ejecutarse como programa principal

    Postcondicion: Muestra el resultado de las pruebas
    
    """

    print("Pruebas")

    lista1 = [1,1,2,3]
    lista1_normalizada = _normalizar(lista1)
    print(f"lista: {lista1}, lista normalizada: {lista1_normalizada}")

    lista2 = [1]
    lista2_normalizada = _normalizar(lista2)
    print(f"lista: {lista2}, lista normalizada: {lista2_normalizada}")

main()