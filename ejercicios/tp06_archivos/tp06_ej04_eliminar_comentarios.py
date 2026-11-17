def _buscar_comentario(linea: str) -> int:
    """
    Contrato: Busca en una línea de codigo la posición del signo #, sin tener en cuenta los que se encuentran encerrados en comillas

    Precondición: linea debe ser una cadena de texto

    Postcondición: Devuelve la posición del # que inicia el comentario o -1 si la línea no tiene comentario
    """
    comillas = ""
    posicion = 0
    comentario = -1

    while comentario == -1 and posicion < len(linea):
        caracter = linea[posicion]

        if comillas != "":
            if caracter == "\\":
                posicion += 1
            elif caracter == comillas:
                comillas = ""
        else:
            if caracter == "'" or caracter == '"':
                comillas = caracter
            elif caracter == "#":
                comentario = posicion

        posicion += 1

    return comentario


def _nombre_salida(nombre_archivo: str) -> str:
    """
    Contrato: Genera el nombre del archivo de salida agregando el sufijo _sin_comentarios al nombre original

    Precondición: nombre_archivo debe ser una cadena de texto

    Postcondición: Devuelve el nombre del archivo de salida
    """
    posicion_punto = nombre_archivo.rfind(".")

    if posicion_punto <= 0:
        base = nombre_archivo
        extension = ""
    else:
        base = nombre_archivo[:posicion_punto]
        extension = nombre_archivo[posicion_punto:]

    return base + "_sin_comentarios" + extension


def _sacar_comentarios(nombre_entrada: str, nombre_salida: str) -> int:
    """
    Contrato: Copia un programa a otro archivo sin sus comentarios, las líneas que solo tienen un comentario se eliminan y las que tienen codigo y comentario se conserva solo el código

    Precondición: nombre_entrada debe ser el nombre de un archivo de texto con código python y nombre_salida el nombre del archivo a generar

    Postcondición: Crea o sobrescribe el archivo de salida sin comentarios y devuelve la cantidad de comentarios eliminados o -1 si no se pudo leer el archivo de entrada o crear el archivo de salida
    """
    eliminados = 0

    try:
        with open(nombre_entrada, "rt", encoding="utf-8-sig") as archivo_entrada:
            with open(nombre_salida, "wt", encoding="utf-8") as archivo_salida:
                linea = archivo_entrada.readline()

                while linea != "":
                    texto = linea.rstrip("\n")
                    posicion = _buscar_comentario(texto)

                    if posicion == -1:
                        archivo_salida.write(linea)
                    else:
                        eliminados += 1
                        codigo = texto[:posicion].rstrip()

                        if codigo != "":
                            archivo_salida.write(codigo + "\n")

                    linea = archivo_entrada.readline()
    except FileNotFoundError:
        eliminados = -1

    return eliminados


def main() -> None:
    """
    Contrato: Ejecuta el programa principal, pide un nombre de archivo con código python y genera una copia del codigo sin comentarios

    Precondición: El archivo debe ejecutarse como programa principal

    Postcondición: Genera el archivo sin comentarios y muestra la cantidad de comentarios elimindaso o mensaje de error
    """
    print("Eliminación de comentarios de un programa python")

    nombre_entrada = input("Nombre del archivo python: ").strip()
    nombre_salida = _nombre_salida(nombre_entrada)

    eliminados = _sacar_comentarios(nombre_entrada, nombre_salida)

    if eliminados == -1:
        print(f"Error, no se pudo leer {nombre_entrada} o crear {nombre_salida}")
    else:
        print(f"Comentarios eliminados: {eliminados}")
        print(f"Archivo generado: {nombre_salida}")


main()
