# Verificación para participar en un concurso internacional

# Solicitar datos al usuario
edad = int(input("Ingrese su edad: "))
pais = input("Ingrese su país: ").strip()
documento = int(input("Ingrese su número de documento: "))

# Verificar condiciones
if 18 <= edad <= 30 and pais.lower() != "antártida" and documento != 0:
    print("Cumple con las condiciones para participar en el concurso.")
else:
    print("No cumple con las condiciones para participar en el concurso.")