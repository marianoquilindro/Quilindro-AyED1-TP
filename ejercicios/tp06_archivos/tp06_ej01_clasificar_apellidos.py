def _leer_personas(nombre_archivo: str) -> list:
    """
    Contrato: Lee un archivo y devuelve sus registros

    Precondición: nombre_archivo es un string con el nombre de un archivo

    Postcondición: Devuelve una lista con los registros del archivo o una lista vacía si el archivo no existe
    """
    personas = []

    try:
        with open(nombre_archivo, "rt", encoding="utf-8-sig") as archivo:
            linea = archivo.readline()

            while linea != "":
                linea = linea.strip()

                if linea != "":
                    personas.append(linea)

                linea = archivo.readline()

    except FileNotFoundError:
        print(f"Error: el archivo {nombre_archivo} no existe")

    return personas


def _filtrar_personas(personas: list, sufijo: str) -> list:
    """
    Contrato: Selecciona las personas que el apellido termina con un sufijo dado

    Precondición: personas tiene que ser una lista de string con formato "apellido, nombre" y sufijo un string

    Postcondición: Deuelve una lista con las personas que su apellido termina con el sufijo
    """
    filtrado = []

    for persona in personas:
        apellido = persona.split(",")[0].strip().lower()

        if apellido.endswith(sufijo.lower()):
            filtrado.append(persona)

    return filtrado


def _exportar_personas(personas: list, nombre_archivo: str) -> None:
    """
    Contrato: Guarda nombres de personas en un archivo de texto

    Precondición: personas tiene que ser una lista de strings y nombre_archivo un string

    Postcondición: Crea o sobrescribe el archivo con los datos recibidos
    """

    try:
        with open(nombre_archivo, "wt", encoding="utf-8") as archivo:
            for persona in personas:
                archivo.write(persona + "\n")
    except FileNotFoundError:
        print(f"Error: no se pudo crear el archivo {nombre_archivo}")


def main() -> None:
    """
    Contrato: Ejecuta el programa principal, lee personas de un archivo y las guarda en nuevos archivos según la terminación de su apellido

    Precondición: El archivo debe ejecutarse como programa principal

    Postcondición: Genera los archivos necesarios y mustra cuantos registros de guardo en cada archivo
    """
    paises = (("Ian", "Armenia.txt"), ("Ini", "Italia.txt"), ("Ez", "España.txt"))

    personas = _leer_personas("personas.csv")

    for sufijo, nombre_archivo in paises:
        filtrado = _filtrar_personas(personas, sufijo)
        _exportar_personas(filtrado, nombre_archivo)
        print(f"{nombre_archivo}: {len(filtrado)} personas")


main()
