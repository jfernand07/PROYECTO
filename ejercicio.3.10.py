# Solicitar la hora del día al usuario
hora = int(input("Introduce la hora del día (número entre 0 y 23): "))

# Verificar si la hora está en el horario permitido
if 8 <= hora <= 18 and hora != 13:
    print("Es horario permitido para clases.")
else:
    print("No es horario permitido para clases.")