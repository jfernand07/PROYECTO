#control de acceso con doble autenticacion

print(" Registrate")
cc =int(input("ingresa tu cedula :"))
nombre= input("cual es tu nombre :")
ingcontraseña= int(input("ingresa una contraseña numerica :"))

print (" inicio de sesion")

cedul= int( input( " ingresa tu cedula :"))
nomb1= input("ingresa tu nombre :")
contraseña = int(input(" ingresa contraseña : "))
if cedul == cc :
    print ("usario correcto") 
    if nombre.lower() == nomb1.lower():
        print ("nombre Correcto")
        if contraseña == ingcontraseña:
                print ("contraseña correta")
        else:
                print("contraseña incorrecta")
    else:
        print("mera vuelta")
        
else:
    print ("Usuario in correcto")