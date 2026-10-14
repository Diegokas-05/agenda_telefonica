agenda = {
}


def leer_entero(mensaje):
    while True:
        try:
            entero = int(input(mensaje))
            return entero
        except(ValueError):
            print("Error intente de nuevo")

def validar_nombre(mensaje):
    while True:
        try:
            nombre = ""
            string = str(input(mensaje)).split()

            for validar in string:
                nombre = nombre + validar.capitalize() + " "

            string = nombre
            if string.replace(" ", "").isalpha():
                print(string)
                return nombre.strip()
            else:
                print("Error intente de nuevo")
        except(AttributeError):
            print("Error intente de nuevo")



def validar_Fon(mensaje):
    while True:
        telefono = input(mensaje)
        if len(telefono) == 8 and telefono.isdigit():
            telefono = str(f"+503{telefono}")
            return telefono
        else:
            print("Error intente de nuevo")



while True:
    
    print("#"* 15, "Mi agenda","#"* 15 )
    print("1: Ver contactos \n" \
    "2: Buscar contacto \n" \
    "3: Agregar contacto \n" \
    "4: Actualizar contacto \n" \
    "5: Eliminar contacto \n" \
    "6: Salir")

    opcion = leer_entero("Ingrese una opcion: ")

    match opcion:
        case 1:
            if len(agenda) > 0:
                for nombre,telefono in agenda.items():
                    print(f"Nombre: {nombre}, Telefono: {telefono}")
            else:
                print("No hay contactos disponibles")
        case 2:
            busqueda = validar_nombre("Ingrese el nombre del contacto: ")
            if busqueda in agenda:
                telefono = agenda[busqueda]
                print(f"El numero es {telefono}")
            else:
                print("El contacto no esta registrado")
        case 3:
            nombre = validar_nombre("Ingrese el nombre: ")
            if nombre in agenda:
                print("Este contacto ya esta registrado")
            else:
                telefono = validar_Fon("Ingrese el numero telefonico: ")
                agenda[nombre] = telefono
                print(f"El contacto {nombre} agregado con exito. ")
        case 4:
            nombre = validar_nombre("Ingrese el nombre: ")
            if nombre in agenda:
                telefono = validar_Fon("Ingrese el numero telefonico: ")
                agenda[nombre] = telefono
                print(f"Su nuevo numero de telefono es {telefono}")
                print(type(telefono))
            else:
                print("Este contacto no esta registrado")
            
        case 5:
            if len(agenda) > 0 :
                nombre = validar_nombre("Ingrese el nombre: ")
                if nombre in agenda:
                    agenda.pop(nombre)
                    print(f"El contacto {nombre} fue borrado con exito")
                else:
                    print("Contacto no encontrado")
            else:
                print("Usted no cuenta con contactos para borrar")
        case 6:
            break
        case _:
            print("Error")