def _validar_mail(mail: str) -> bool:
    """
    Contrato: determina si una dirección de email es valida

    Precondición: mail debe ser un string

    Postcondición: Devuelve True si la direccion es válida, False si no lo es
    """

    email = mail.strip().lower()

    posicion_arroba = email.find("@")

    if posicion_arroba == -1 or posicion_arroba == 0:
        return False

    if email.find("@", posicion_arroba + 1) != -1:
        return False

    usuario = email[:posicion_arroba]
    dominio = email[posicion_arroba + 1 :]

    if not usuario.isalnum():
        return False

    if dominio.endswith(".com.ar"):
        largo_sufijo = 7
    elif dominio.endswith(".com"):
        largo_sufijo = 4
    else:
        return False

    return len(dominio) > largo_sufijo


def main() -> None:
    """
    Contrato: Ejecuta el programa principal, lee direcciones de email hasta que se ingresa un string vacio, indica si un email es válido y mustra los emails válidos sin repetir y en orden alfabético

    Precondición: El archivo debe ejecutarse como programa principal

    Postcondición: Muestra el resultado de cada validación y la lista de emails
    """

    print("Validación de direcciones de emails")

    dominios = []

    mail = input("Ingrese una dirección de correo: ").strip().lower()

    while mail != "":
        if _validar_mail(mail):
            print("Dirección de correo válida")

            dominio = mail[mail.find("@") + 1 :]
            if dominio not in dominios:
                dominios.append(dominio)
        else:
            print("La dirección de correo no es válida")

        mail = input("Ingrese una dirección de correo: ").strip().lower()

    dominios.sort()

    if len(dominios) == 0:
        print("No se ingresaron direcciones válidas")
    else:
        print("Dominios de las direcciónes válidas")
        print(dominios)


main()
