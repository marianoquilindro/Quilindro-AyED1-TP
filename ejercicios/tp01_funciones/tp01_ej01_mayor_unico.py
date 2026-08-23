def _mayor_unico(v1: int,v2: int,v3: int) -> int:
    """
    Contrato: Determina el valor mayor unico entre tres numeros

    Precondicion: v1, v2 y v3 deben ser enteros positivos
    
    Postcondicion: Devuelve el valor mayor unico entre v1, v2 y v3, o, -1 si hay un empate en el valor maximo
    """
    if (v1 == v3 and v1 >= v3) or (v1 == v3 and v1 >= v2) or (v2 == v3 and v2 >= v1):
        return -1

    if v1 > v2 and v1 > v3:
        return v1
    elif v2 > v1 and v2 > v3:
        return v2
    else:
        return v3


while True:
    valor1 = int(input('ingrese un valor numerico positivo (del 1 al 100): '))
    valor2 = int(input('ingrese un valor numerico positivo (del 1 al 100): '))
    valor3 = int(input('ingrese un valor numerico positivo (del 1 al 100): '))
    if valor1 > 0 and valor2 < 100 and valor2 > 0 and valor1 < 100 and valor3 > 0 and valor3 < 100:
        break

print(_mayor_unico(valor1,valor2,valor3)) 