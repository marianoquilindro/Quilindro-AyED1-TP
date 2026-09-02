import random as rn

def _cargar_lista () -> list:
    """
    Contrato: Carga una lista con números al azar de cuatro digitos, la cantidad de elementos tambien es un número al azar de dos digitos

    Precondiciones: Se debe importar la libreria random para el uso de la función

    Postcondicion: Devuelve una lista de números enteros de cuatro digitos, con una cantidad de elementos de dos digitos
    
    """
    cantidad = rn.randint(10,99)
    lista = []

    contador = 0
    while contador < cantidad:
        valor = rn.randint(1000,9999)
        lista.append(valor)
        contador += 1

    return lista

def _calcular_producto (lista: list) -> int:
    """
    Contrato: Calcula la multiplicación de todos los elementos de la lista

    Precondicion: lista debe tener al menos un elemento

    Postcondicion: Devuelve la multiplicación de todos los elementos de la lista
    
    """
    producto = 1

    indice = 0
    while indice < len(lista):
        producto = producto * lista[indice]
        indice += 1

    return producto

def _borrar_apariciones (lista: list, valor: int) -> None:
    """
    Contrato: Elimila todas las apariciones de un valor en la lista

    Precondiciones: lista tiene que ser una lista de enteros

    Postcondicion: La lista queda modificada, borrando todas las apariciones del valor indicado
    
    """
    while valor in lista:
        lista.remove(valor)


def _es_capicua (lista: list) -> bool:
    """
    Contrato: Determina si una lista es capicua
    
    Precondiciones: lista tiene que ser una lista de enteros

    Postcondiciones: Devuele True si la lista es capicua o False si no lo es
    
    """

    izquierda = 0
    derecha = len(lista) -1

    while izquierda < derecha:
        if lista[izquierda] != lista[derecha]:
            return False
        izquierda += 1
        derecha -= 1

    return True

def main() -> None:
    """
    Contrato: Ejecuta el programa principal, invoca funciones y muestra los resultados
    
    Precondicion: El archivo debe ejecutarse como programa principal

    Postcondiciones: Muestra el resultado de cada operación
    
    """

    print("Carga de lista de manera random")

    lista = _cargar_lista()
    print(f"lista cargada de {len(lista)} elementos:")
    print(lista)

    print("Cálculo de producto de elementos de una lista")

    producto = _calcular_producto(lista)
    print(f"Producto de los elementos: {producto}")

    print("Eliminar un valor de la lista")

    print(lista)
    valor_borrar = int(input("Ingrese un valor de la lista para eliminar sus apariciones: "))
    _borrar_apariciones(lista, valor_borrar)
    print("Lista luego de eliminar el valor ingresado:")
    print(lista)

    print("Listas capicuas")

    lista_capicua = [10,20,30,20,10]
    lista_no_capicua = [10,20,30,40,50]
    print(f"La lista {lista_capicua} es capicua?: {_es_capicua(lista_capicua)}")
    print(f"La lista {lista_no_capicua} es capicua?: {_es_capicua(lista_no_capicua)}")

main()