def _convertir_formato1(nombre_entrada: str, nombre_salida: str) -> None:
    """
    Contrato: Lee un archivo de longitud fija y guarda sus registros en formato csv, sacando los espacios que sobran en el final de cada campo

    Precondición: nombre_entrada debe ser un archivo de texto en formato1 y nombre_salida es el nombre del archivo csv a generar

    Postcondición: Crea o sobrescribe el archivo csv con un registro por linea
    """

    try:
        with open(nombre_entrada, "rt", encoding="utf-8-sig") as archivo_entrada:
            with open(nombre_salida, "wt", encoding="utf-8") as archivo_salida:
                linea = archivo_entrada.readline()

                while linea != "":
                    linea = linea.rstrip("\n")

                    if linea.strip() != "":
                        apellido_nombre = linea[0:16].strip()
                        fecha = linea[17:25].strip()
                        domicilio = linea[26:].strip()

                        archivo_salida.write(
                            ",".join([apellido_nombre, fecha, domicilio]) + "\n"
                        )

                    linea = archivo_entrada.readline()

    except FileNotFoundError:
        print(f"Error: no se pudo leer {nombre_entrada} o crear {nombre_salida}")


def _separar_campos_formato2(linea: str) -> list:
    """
    Contrato: Separa los campos de un registro del formato 2, en el que cada campo tiene adelante dos dígitos que indican su longitud

    Precondición: linea debe ser una cadena de texto

    Postcondición: Devuelva una lista de los campos del registro
    """
    campos = []
    posicion = 0

    while posicion < len(linea):
        largo = int(linea[posicion : posicion + 2])
        posicion += 2

        if posicion + largo > len(linea):
            raise ValueError("El campo excede el largo de la línea")

        campos.append(linea[posicion : posicion + largo])
        posicion += largo

    return campos


def _convertir_formato2(nombre_entrada: str, nombre_salida: str) -> None:
    """
    Contrato: Lee un archivo en el que cada campo tiene al comienzo un numero de dos dígitos que indica su longitud y graba sus registros en formato csv

    Precondición: nombre_entrada debe ser un archivo de texto en formato 2 y nombre_salida es el nombre del archivo csv a generar

    Postcondición: Crea o sobrescribe el archivo csv
    """

    try:
        with open(nombre_entrada, "rt", encoding="utf-8-sig") as archivo_entrada:
            with open(nombre_salida, "wt", encoding="utf-8") as archivo_salida:
                linea = archivo_entrada.readline()

                while linea != "":
                    linea = linea.rstrip("\n")

                    if linea.strip() != "":
                        try:
                            campos = _separar_campos_formato2(linea)
                            archivo_salida.write(",".join(campos) + "\n")

                        except ValueError:
                            print(f"Registro inválido, se omite {linea}")

                    linea = archivo_entrada.readline()

    except FileNotFoundError:
        print(f"Error: no se pudo leer {nombre_entrada} o crear {nombre_salida}")


def main() -> None:
    """
    Contrato: Ejecuta el programa principal, convierte en formato csv los archivos empleados en formato 1 y 2

    Precondición: El archivo debe ejecutarse como programa principal

    Postcondición: Genera empleados_formato1.csv y empleados_formato2.csv a partir de sus archivos de texto
    """

    print("Conversión de archivos de empleados a formato csv")

    _convertir_formato1("empleados_formato1.txt", "empleados_formato1.csv")
    _convertir_formato2("empleados_formato2.txt", "empleados_formato2.csv")

    print("Conversión finalizada")


main()
