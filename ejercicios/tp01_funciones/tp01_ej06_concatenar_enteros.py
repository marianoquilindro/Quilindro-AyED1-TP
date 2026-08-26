def _contar_digitos (numero: int) -> int:
    """
    Contrato: Cuenta la cantidad de dígitos que tiene un numero entero positivo
    
    Precondiciones: La variable numero debe ser un numero entero positivo

    Postcondiciones: Devuelve la cantidad de dígitos del numero

    """
    contador = 0 
    while numero > 0:
        numero = numero // 10
        contador += 1
    return contador


def _concatenar (a: int, b: int) -> int:
    """
    Contrato: Concatena dos números enteros positivos devolviendo el numero que se obtiene al unir sus digitos
    
    Precondicion: a y b deben ser enteros positivos

    Postcondiciones: Devuelve el numero obtenido al concatenar a y b
    
    """
    digitos_b = _contar_digitos(b) 
    return a * (10 ** digitos_b) + b


def main() -> None:
    """
    Contrato: Ejecuta el programa principal, solicita dos numeros al usuario y muestra el resultado de concatenarlos
    
    Precondicion: El archivo debe ejecutarse como programa principal

    Postcondicion: Muestra el número que se obtiene de la concatenación 
    
    """

    print("Concatenación de números")

    primer_numero = int(input("Ingrese el primer número: "))
    segundo_numero = int(input("Ingrese el segundo número: "))

    resultado = _concatenar(primer_numero,segundo_numero)

    print(f"El resultado de concatenar {primer_numero} y {segundo_numero} es {resultado}")

main()