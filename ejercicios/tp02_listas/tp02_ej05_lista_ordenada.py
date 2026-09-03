def _ordenada (lista: list) -> bool:
    """
    Contrato: Determina si una lista esta ordenada en forma ascendente

    Precondicion: lista debe ser homogenea 

    Postcondicion: Devuelve True si la lista esta ordenada en forma ascendente, False en caso de que no
    
    """
    indice = 0
    while indice < len(lista) -1:
        if lista[indice] > lista[indice + 1]:
            return False
        indice += 1
    return True


def main() -> None:
    """
    Contrato: Ejecuta el programa principal, verifica el comportamiento de la funcion
    
    Precondicion: El archivo debe ejecutarse como programa principal

    Postcondicion: Muestra el resultado de las pruebas
    
    """

    print("Pruebas")

    lista_ordenada_int = [1,2,3,4,5]
    print(f"{lista_ordenada_int} esta ordenada?: {_ordenada(lista_ordenada_int)}")

    lista_ordenada_str = ["a","b","c","d"]
    print(f"{lista_ordenada_str} esta ordenada?: {_ordenada(lista_ordenada_str)}")


    lista_desordenada_int = [1,3,2,5,4]
    print(f"{lista_desordenada_int} esta ordenada?: {_ordenada(lista_desordenada_int)}")

    lista_desordenada_str = ["a","c","b","d"]
    print(f"{lista_desordenada_str} esta ordenada?: {_ordenada(lista_desordenada_str)}")

main()

