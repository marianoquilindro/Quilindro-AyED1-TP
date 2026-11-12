def _separar_direccion(direccion: str) -> tuple:
    """
    Contrato: Separa una dirección de correo en nombre de usuario y cada una de las partes del dominio separadas por puntos

    Precondición: direccion debe ser una cadena de texto

    Postcondición: Devuelve una tupla con el usuario seguido de las partes del dominio o una tupla vacía si el formato de la dirección no es válida
    """

    partes = ()

    if direccion.count("@") == 1 and " " not in direccion:
        usuario, dominio = direccion.split("@")
        subdominios = dominio.split(".")

        if usuario != "" and len(subdominios) >= 2 and "" not in subdominios:
            partes = (usuario,) + tuple(subdominios)

    return partes


def main() -> None:
    """
    Contrato: Ejecuta el programa principal, lee direcciones de correo hasta que se ingresa una cadena vacía y muestra las partes de cada una o un aviso si el formato no es válido

    Precondición: El archivo debe ejecutarse como programa principal

    Postcondición: Muestra la tupla con las partes de cada dirección válida o un mensaje de error
    """
    print("Partes de una dirección de correo")

    direccion = input("Ingrese una dirección (vacío para terminar): ").strip()

    while direccion != "":
        partes = _separar_direccion(direccion)

        if len(partes) == 0:
            print("El formato de la dirección no es válido")
        else:
            print(f"Partes: {partes}")

        direccion = input("Ingrese una dirección (vacío para terminar): ")


main()
