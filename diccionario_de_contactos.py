print("Diccionario de contactos")
def menu ():
    while True:
        print("Bienvenido escoge la opcion que deseas realizar")
        print("1. agregar contacto")
        print("2. ver contactos")
        print("3. buscar contacto")
        print("4. Eliminar contacto")
        print("5.salir")
        opcion=(input("ingresa el numero de la opcion que deseas:"))
        match opcion:
            case "1":
                agregar_contacto()
            case "2":
                ver_contactos()
            case "3":
                buscarcontac()
            case "4":
                borrarcontac()
            case "5" :
                print ("has salido del programa")
                break
            case _:
                print("Opción no válida")
            
    
contactos={}

def agregar_contacto():
    while True:
        
        try:
            nombre=input("Ingresar nombre: ").title()
            cel=int(input("Ingresar numero de telefono: "))
            
            contactos[nombre]=cel
        except ValueError:
            print("Por favor ingresa un número de télefono válido")
        print(f"{nombre}agregado con exito",)
        
        menu()
def ver_contactos():
    if not contactos:
        
     print("No hay contactos")
     
    else:
        print(contactos)
        menu()
    
            
def  buscarcontac():  
    nombre=input("Ingresa el nombre del contacto: ").title()
    if not nombre in contactos:
        print("no se encontro ningun contacto")
    else:
        print (f"Nombre:{nombre} , télefono: {contactos[nombre]}")
        
        menu()
        
def borrarcontac():
    nombre=input("Ingresa el nombre del contacto: ").title()
    if not nombre in contactos:
        print("no se encontro ningun contacto")
    else:
        for nombre in contactos:
            contactos.pop(nombre)
            print(f"contacto , '{nombre}', Eliminado")
            menu()
menu()
    
    

    