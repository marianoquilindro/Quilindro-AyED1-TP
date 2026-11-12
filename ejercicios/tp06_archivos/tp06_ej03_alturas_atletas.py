def _grabar_rango_alturas(nombre_archivo: str) -> None:
    """
    Contrato: Solicita disciplinas deportivas y las alturas de los atletas de esa disciplina, y las guarda en un archivo de texto

    Precondición: nombre_archivo es un string con el nombre del archivo a generar

    Postcondición: Crea o sobrescribe el archivo con las disciplinas y las alturas
    """

    try:
        with open(nombre_archivo, "wt", encoding="utf-8") as archivo:
            disciplina = input("Disciplina (vacío para terminar): ").strip()

            while disciplina != "":
                archivo.write(disciplina + "\n")
                altura = (
                    input(
                        "Altura del atleta en mts (vacío para pasar a otra disciplina): "
                    )
                    .strip()
                    .replace(",", ".")
                )

                while altura != "":
                    try:
                        float(altura)
                        archivo.write(altura + "\n")
                    except ValueError:
                        print("Debe ingresar un número válido")

                    altura = (
                        input(
                            "Altura del atleta en mts (vacío para pasar a otra disciplina): "
                        )
                        .strip()
                        .replace(",", ".")
                    )

                disciplina = (
                    input(
                        "Disciplina (vacío para terminar): "
                    )
                    .strip()
                    .replace(",", ".")
                )
    except FileNotFoundError:
        print(f"Error: no se pudo crear el archivo {nombre_archivo}")


def _grabar_promedio(nombre_alturas: str, nombre_promedios: str) -> None:
    """
    Contrato: Lee el archivo de alturas, calcula el promedio de alturas de cada disciplina y lo guarda en otro archivo

    Precondición: nombre_altura debe ser el archivo generado por _grabar_rango_altura y nombre_promedios el archivo a generar

    Postcondición: Crea o sobrescribe el archivo de promedios
    """

    try:
        with open(nombre_alturas, "rt", encoding="utf-8-sig") as archivo_entrada:
            with open(nombre_promedios, "wt", encoding="utf-8") as archivo_salida:
                disciplina = ""
                suma = 0
                cantidad = 0

                linea = archivo_entrada.readline()

                while linea != "":
                    linea = linea.strip()

                    if linea != "":
                        try:
                            suma += float(linea)
                            cantidad += 1
                        except ValueError:
                            if cantidad > 0:
                                archivo_salida.write(disciplina + "\n")
                                archivo_salida.write(
                                    str(round(suma / cantidad, 2)) + "\n"
                                )

                            disciplina = linea
                            suma = 0
                            cantidad = 0

                    linea = archivo_entrada.readline()

                if cantidad > 0:
                    archivo_salida.write(disciplina + "\n")
                    archivo_salida.write(str(round(suma / cantidad, 2)) + "\n")

    except FileNotFoundError:
        print(f"Error: no se pudo leer {nombre_alturas} o crear {nombre_promedios}")


def _mostrar_mas_altos(nombre_promedios: str) -> None:
    """
    Contrato: Lee el archivo de promedios y calcula la estatura promedio general, y muestra las disciplinas que el promedio la supera

    Precondición: nombre_promedios debe ser el archivo generado por _grabar_promedio

    Postcondición: Muestra la estatura promedio general y las disciplinas que la superan
    """
    disciplinas = []
    promedios = []

    try:
        with open(nombre_promedios, "rt", encoding="utf-8-sig") as archivo:
            disciplina = archivo.readline().strip()

            while disciplina != "":
                promedios.append(float(archivo.readline().strip()))
                disciplinas.append(disciplina)

                disciplina = archivo.readline().strip()

    except FileNotFoundError:
        print(f"Error: el archivo {nombre_promedios} no existe")

    if len(promedios) == 0:
        print("No hay datos")
    else:
        promedio_general = sum(promedios) / len(promedios)
        print(f"Estatura promedio general: {round(promedio_general, 2)}")

        print("Disciplinas que superan la estatura promedio general:")

        hay_alguna = False

        for i in range(len(disciplinas)):
            if promedios[i] > promedio_general:
                print(f"{disciplinas[i]} promedio: {promedios[i]}")
                hay_alguna = True

        if not hay_alguna:
            print("Ninguna disciplina supera el promedio general")


def main() -> None:
    """
    Contrato: Ejecuta el programa principal, guarda disciplinas, las alturas de los atletas, calcula promedios por disciplinas y muestra las disciplinas que superan el promedio general de altura

    Postcondición: El archivo debe ejecutarse como programa principal

    Precondición: Genera los archivos alturas.txt y promedios.txt
    """
    print("Clasificación de atletas por disciplina")

    _grabar_rango_alturas("alturas.txt")
    _grabar_promedio("alturas.txt", "promedios.txt")
    _mostrar_mas_altos("promedios.txt")


main()
