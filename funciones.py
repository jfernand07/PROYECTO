#Diccionarios
#rea una pequeña agenda que permita:
#Agregar un nuevo contacto (nombre y número de teléfono).
#Buscar un contacto por su nombre.
#Mostrar todos los contactos.
#Eliminar un contacto.
#📦 Requisitos
#   Usar un diccionario donde el nombre sea la clave y el número sea el valor.
#  Crear un pequeño menú en consola para elegir las acciones.
cuentas=[]
#diccionario X


while True:
    print("bienvenido al menu")
    print("que desea hacer")
    print("1. agregar nuevo contacto" , "\n2. eliminar contacto", "\n3.buscar contacto" , "\n4.ver lista" , "\n5.salir")

    opciones=int(input("escribe la opcion que deseas: "))
    if opciones== 1 :
        nombre = input("ingresa el nombre del contacto nuevo :") .lower()
        print("nombre guardado con exito")
        celular= int(input("ingresa tu celular :"))
        print("numero ingresado con Exito")
        edad= int(input("cual es tu edad :"))
        print("edad ingresada correctamente")
        contacto={"nombre": nombre, "celular" : celular, "edad": edad}
        cuentas.append(contacto)   
        
    elif opciones==2: 
        nombre=input("ingresa el nombre que deseas eliminar :").lower()
        for contacto in cuentas:
            if contacto["nombre"]==nombre:
                confirmacion= input("Deseas eliminar al usuario", {nombre}, "(si /no): ").lower()
                if confirmacion == "si":
                    cuentas.remove(contacto)
                print(f"{nombre} ha sido eliminado de la lista.")
            else:
                print("La eliminación ha sido cancelada.")
            break
        else: 
            print("No se encontro el contacto")
    elif opciones == 3 :
        nombre=input("ingresa el nombre que deseas buscar en la lista :") .lower()
        for contacto in cuentas:
            if contacto["nombre"]==nombre:
                confirmacion= input(f" este es el usuario correto que estas buscando? {nombre}(si/no): " ) .lower ()
                if confirmacion == "si" :
                    print (contacto)
                else:
                    print("Busqueda cancelada")
                break
            else:
                print("No se encontro el contacto")
    elif opciones ==4:
        confirmacion= input("deseas ver toda la lista de datos (si/no)") .lower()
        if confirmacion== "si":
            print (cuentas)
    elif opciones== 5:
        print("saliendo del programa")
        break
    else:
        print("Opcion no valida. Por favor, elige una opcion del 1 al 5")









