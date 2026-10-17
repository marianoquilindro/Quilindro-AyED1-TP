def _ultimos_n_caracteres(cadena: str, n: int) -> str:
    """
    Contrato: Devuelve una subcadena con los ultimos n caracteres de una cadena

    Precondición: cadena debe ser un string y n un entero mayor o igual a 0

    Postcondición: Devuelve los ultimos n caracteres o la cadena completa si n es mayor o igual a la longitud de la cadena
    """
    if n >= len(cadena):
        inicio = 0
    else:
        inicio = len(cadena) - n

    return cadena[inicio:]


def main() -> None:
    """
    Contrato: Ejecuta el programa principal, solicita una cadena y un valor de n y muestra la cadena resultante de usar la función

    Precondición: El archivo debe ejecutarse como programa principal

    Postcondición: Muestra el resultado del uso de la función
    """

    print("Ultimos N caracteres de una cadena")

    cadena = input("Ingrese una cadena de caracteres: ")
    n = int(input("Ingrese el valor de N: "))

    print(f"Los ultimos {n} caracteres son: {_ultimos_n_caracteres(cadena,n)}")

main()