def _cargar_lista() -> list:
    """
    Contrato: Carga una lista con números enteros ingresados por el usuario, la carga se finaliza cuando el usuario ingresa -1
    
    Precondiciones: El usuario debe ingresar numeros enteros

    Postcondicion: Devuelve una lista con los numeros ingresados, excluyendo el -1
    
    """
    lista =[]

    numero = int(input("ingrese un número (-1 para terminar): "))

    while numero != -1:
        lista.append(numero)
        numero = int(input("ingrese un número (-1 para terminar): "))

    return lista

def _eliminar_valores (lista_original: list, lista_valores: list) -> None:
    """
    Contrato: Elimina de la lista original todas las apariciones de un valor que este en la losta de valores a eliminar

    Precondicion: Ambas listas deben contener enteros
    
    Postcondicion: La lista original queda modificada sin las apariciones de los valores de la segunda lista
    
    """
    for valor in lista_valores:
        while valor in lista_original:
            lista_original.remove(valor)


def main() -> None:
    """
    Contrato: Ejecuta el programa principal, solicita al usuario la carga de dos listas
    
    Precondicion: El archivo debe ejecutarse como programa principal

    Postcondicion: Muestra la lista cargada, los valores a eliminar y como queda la lista luego de eliminar los valores
    
    """

    print("Carga de la lista original")
    lista_original = _cargar_lista()

    print("Carga de la lista de valores a borrar")
    lista_valores = _cargar_lista()

    print(f"lista original: {lista_original}")
    print(f"lista de valores a borrar: {lista_valores}")

    _eliminar_valores(lista_original,lista_valores)

    print(f"resultado: {lista_original}")

main()