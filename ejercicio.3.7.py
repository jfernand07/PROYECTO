# Solicitar estatura y edad al usuario
estatura = int(input("Ingrese su estatura en cm: "))
edad = int(input("Ingrese su edad: "))

# Verificar si cumple con los requisitos para ingresar
if estatura > 140 and 10 <= edad <= 60:
    print("¡Puede ingresar a la atracción!")
else:
    print("Lo sentimos, no cumple con los requisitos para ingresar.")