def _imprimir_numeros(limite: int) -> None:
    """
    Contrato: Imprime los números enteros entre 1 y el límite ingresado, si el usuario presiona ctrl + c pide confirmación al usuario

    Precondición: limite debe ser un número entero mayor o igual a 1

    Postcondición: Muestra por pantalla los números impresos hasta finalizar la secuencia o que el usuario la frene
    """

    numero = 1
    continuar = True

    while continuar and numero <= limite:
        try:
            print(numero)
            numero += 1
        except KeyboardInterrupt:
            respuesta = input("Desea detener el programa (si/no)").strip().lower()

            if respuesta == "si":
                continuar = False
                print("Programa detenido por el usuario")
            else:
                print("Continuando ...")


def main() -> None:
    """
    Contrato: Ejecuta el programa principal, imprime números entre 1 y 100000 y maneja la interrupción por teclado

    Precondición: El archivo debe ejecutarse como programa principal

    Postcondición: Muestra los números del 1 al 100000 o hasta que el usuario confirme la interrupción
    """

    print("Impresión de números entre 1 y 100000")

    _imprimir_numeros(100000)


main()
