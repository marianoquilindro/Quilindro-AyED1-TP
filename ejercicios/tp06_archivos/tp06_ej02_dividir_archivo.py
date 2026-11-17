def _longitud_maxima_registro(nombre_archivo: str) -> int:
    """
    Contrato: Recorre un archivo y determina la longitud en caracteres del registro más largo

    Precondición: nombre_archivo debe ser una cadena con el nombre de un archivo de texto

    Postcondición: Devuelve la longitud del registro mas largo, 0 si el archivo esta vacío, -1 si el archivo no existe o -2 si no esta codificado en utf-8
    """
    maximo = 0

    try:
        with open(nombre_archivo, "rt", encoding="utf-8-sig") as archivo:
            registro = archivo.readline()

            while registro != "":
                if len(registro) > maximo:
                    maximo = len(registro)

                registro = archivo.readline()

    except FileNotFoundError:
        maximo = -1
    except UnicodeDecodeError:
        maximo = -2

    return maximo


def _nombre_parte(nombre_archivo: str, numero_parte: int) -> str:
    """
    Contrato: Genera el nombre de una parte agregando al nombre un sufijo que indica en número de parte

    Precondición: nombre_archivo debe ser una cadena de texto y numero_parte un número entero

    Postcondición: Devuelve el nombre de la parte (ej "datos.txt" con la parte 2 queda "datos_parte2.txt)
    """
    posicion_punto = nombre_archivo.rfind(".")

    if posicion_punto <= 0:
        base = nombre_archivo
        extension = ""
    else:
        base = nombre_archivo[:posicion_punto]
        extension = nombre_archivo[posicion_punto:]

    return base + "_parte" + str(numero_parte) + extension


def _dividir_archivo(nombre_archivo: str, tamanio_maximo: int) -> int:
    """
    Contrato: Divide un archivo en partes de tamanio_maximo caracteres

    Precondición: nombre archivo debe ser una cadena con el nombre de un archivo de texto y tamanio_maximo un núemero entero mayor o igual a la longitud del registro más largo del archivo

    Postcondición: Gener los archivos de las partes y devuelve la cantidad de partes generadas o -1 si el archivo no pudo procesarse
    """
    partes = 0

    try:
        with open(nombre_archivo, "rt", encoding="utf-8-sig") as archivo_entrada:
            registro = archivo_entrada.readline()

            while registro != "":
                partes += 1
                tamanio_parte = 0

                with open(
                    _nombre_parte(nombre_archivo, partes), "wt", encoding="utf-8"
                ) as archivo_salida:
                    while (
                        registro != ""
                        and tamanio_parte + len(registro) <= tamanio_maximo
                    ):
                        archivo_salida.write(registro)
                        tamanio_parte += len(registro)
                        registro = archivo_entrada.readline()
    except FileNotFoundError:
        partes = -1

    return partes


def main() -> None:
    """
    Contrato: Ejecuta el programa principal, pide un nombre de un archivo, el tamaño máximo de las partes y divide el archivo

    Precondición: El archivo debe ejecutarse como programa principal

    Postcondición: Genera los archivos de las partes y muestra la cantidad generada o un mensaje de error si no los pudo generar
    """
    print("División de un archivo de texto en partes")

    nombre_archivo = input("Nombre del archivo a dividir: ").strip()

    try:
        tamanio_maximo = int(input("Tamaño máximo de cada parte (en caracteres): "))
    except ValueError:
        tamanio_maximo = -1

    if tamanio_maximo <= 0:
        print("Error: al tamaño maximo debe ser un número entero positivo")
    else:
        longitud_maxima = _longitud_maxima_registro(nombre_archivo)

        if longitud_maxima == -1:
            print(f"Error: el archivo {nombre_archivo} no existe")
        elif longitud_maxima == -2:
            print("Error: el archivo no se pudo leer")
        elif longitud_maxima == 0:
            print("Error: el archivo está vacío")
        elif longitud_maxima > tamanio_maximo:
            print(
                f"Error: hay un registro de {longitud_maxima} caracteres que supera el tamaño maximo a dividir"
            )
        else:
            partes = _dividir_archivo(nombre_archivo, tamanio_maximo)

            if partes == -1:
                print("Error: no se pudo dividir el archivo")
            else:
                print(f"Archivo dividido en {partes} partes")


main()
