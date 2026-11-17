def _crear_lista_precios() -> dict:
    """
    Contrato: Crea el diccionario con la lista de precios de una librería, donde las claves son los nombres de los productos y los valores sus precios

    Precondición: -

    Postcondición: Devuelve un diccionario con los productos y sus precios
    """
    return {"cuaderno rayado": 1500.0, "cuaderno cuadriculado": 1650.0, "lapicera azul": 450.0, "lapiz negro": 300.0, "goma de borrar": 250.0, "resma de hojas A4": 9800.0}


def _incrementar_precios(precios: dict, palabra: str, porcentaje: float) -> None:
    """
    Contrato: Incrementa en un porcentaje el precio de todos los productos cuyo nombre contiene una palabra, redondeando el nuevo precio a dos decimales

    Precondición: precios debe ser un diccionario de procuto: precio, palabra debe ser una cadena de texto y porcentaje debe ser un número real

    Postcondición: Modifica el diccionario con los nuevos precios de los productos que contienen la palabra
    """
    for producto in precios:
        if palabra.lower() in producto.lower():
            precios[producto] = round(precios[producto] * (1 + porcentaje / 100), 2)


def _producto_mas_costoso(precios: dict) -> tuple:
    """
    Contrato: Busca el producto de mayor precio de la lista, si hay varios con el mismo precio máximo devuelve el primero que aparece

    Precondición: precios debe ser un diccionario producto: precio

    Postcondición: Devuelve una tupla (producto, precio) del mas costoso o ("",0.0) si el diccionario esta vacío
    """
    mas_costoso = ""
    precio_maximo = 0.0

    for producto, precio in precios.items():
        if mas_costoso == "" or precio > precio_maximo:
            mas_costoso = producto
            precio_maximo = precio

    return (mas_costoso,precio_maximo)


def main() -> None:
    """
    Contrato: Ejecuta el programa principal, cera una lista de precios de una librería e incrementa un 1% el precio de los cuadernos

    Precondición: El archivo debe ejecutarse como programa principal

    Postcondición: Muestra la lista original, la lista actualizada y el producto mas costoso
    """
    print("Lista de precios de la librería")

    precios =_crear_lista_precios()

    print("Lista original")
    print(precios)

    _incrementar_precios(precios,"cuaderno", 15)

    print("Lista con los cuadernos icrementados un 15%:")
    print(precios)

    producto, precio = _producto_mas_costoso(precios)

    print(f"El producto mas costoso es: {producto} (${precio})")

main()