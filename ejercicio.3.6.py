# Solicitar datos al usuario
promedio = float(input("Ingresa tu promedio: "))
ingresos = float(input("Ingresa tus ingresos mensuales: "))
materias = int(input("Ingresa la cantidad de materias que estás cursando: "))

# Verificar si aplica a la beca
if promedio >= 8 and materias < 3 and ingresos <= 1500:
    print("¡Felicidades! Aplicas para la beca.")
else:
    print("Lo sentimos, no aplicas para la beca.")