import random as rn


def _jugar(numero_secreto: int, max_intentos: int) -> int:
    """
    Contrato: Solcicita números al usuario hasta que adivine el número secreto o agote los intentos indicando en cada intento si el numero ingresado es mayor o menor al que tiene que adivinar

    Precondición: numero_secreto debe ser un número entero y max_intentos un número entero mayor o igual a 1

    Postcondición: Devuelve la cantidad de intentos que le tomo al usuario adivinar el número o -1 si no lo adivino
    """
    intentos = 0
    adivinado = False

    while not adivinado and intentos < max_intentos:
        entrada = input("ingrese un número entre 1 y 500:")
        intentos += 1

        try:
            numero = int(entrada)

            if numero == numero_secreto:
                adivinado = True
            elif numero_secreto > numero:
                print("El número a adivinar es mayor al ingresado")
            else:
                print("El número a adivinar es menor al ingresado")

        except ValueError:
            print("Lo ingresado no es un número, igualmente suma un intento")

        if not adivinado and intentos < max_intentos:
            print(f"Intentos restantes: {max_intentos - intentos}")

    if not adivinado:
        intentos = -1

    return intentos


def main() -> None:
    """
    Contrato: Ejecuta el programa principal, genera un número al azar entre 1 y 500 y solicita al usuario adivinar el número

    Precondición: El archivo debe ejecutarse como programa principal

    Postcondición: Muestra las pistas de cada intento y la cantidad de intentos al adivinar el número, o el número si se agotan los intentos
    """
    print("Adivinar el número entre 1 y 500")

    numero_secreto = rn.randint(1,500)
    intentos = _jugar(numero_secreto,10)

    if intentos == -1:
        print(f"Te quedaste sin intentos, el número era: {numero_secreto}")
    else:
        print(f"Adivinaste el número en {intentos} intentos")

main()