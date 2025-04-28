# Evaluación académica de estudiante

# Solicitar las dos notas al usuario
nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))

# Verificar si el estudiante aprobó
if nota1 >= 6 and nota2 >= 6 and nota1 >= 4 and nota2 >= 4:
    print("El estudiante aprobó.")
else:
    print("El estudiante no aprobó.")