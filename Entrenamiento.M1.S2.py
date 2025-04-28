#El programa que vas a desarrollar en este entrenamiento debe:

    #Determinar el estado de aprobación:
     #   Solicitar al usuario ingresar una calificación numérica (de 0 a 100)
      #  Evaluar si el estudiante ha aprobado o reprobado basándose en la calificación ingresada
    #Calcular el promedio:
     #   Permitir al usuario ingresar una lista de calificaciones (separadas por comas)
      #  Calcular y mostrar el promedio de las calificaciones en la lista
    #Contar calificaciones mayores:
     #   Preguntar al usuario por un valor específico
     #   Contar cuántas calificaciones en la lista son mayores que este valor
   # Verificar y contar calificaciones específicas:
    #    Permitir al usuario ingresar una lista de calificaciones (separadas por comas)
     #   Calcular y mostrar el promedio de las calificaciones en la lista
     
# DETERMINAR ESTADO DE APROBACIÓN 
calificacion = float(input("Ingresa una calificación numérica (0-100): "))
if calificacion >= 60:
    print("El estudiante ha aprobado.")
else:
    print("El estudiante ha reprobado.")

# INGRESO DE CALIFICACIONES 
entrada = input("\nIngresa una lista de calificaciones separadas por comas: ")
calificaciones = [float(x.strip()) for x in entrada.split(",") if x.strip().isdigit()]

# CÁLCULO DE PROMEDIO 
if len(calificaciones) > 0:
    promedio = sum(calificaciones) / len(calificaciones)
    print(f"\nEl promedio de las calificaciones es: {promedio:.2f}")
else:
    print("No se ingresaron calificaciones válidas.")
    
# PROMEDIO GANO O PERDIO
if promedio> 60 :
    print("Ganó con un valor de" , promedio)

# CONTAR CALIFICACIONES MAYORES QUE UN VALOR 
valor = float(input("\nIngresa un valor para contar cuántas calificaciones son mayores: "))
mayores = 0
for nota in calificaciones:
    if nota > valor:
        mayores += 1
print(f"Cantidad de calificaciones mayores que {valor}: {mayores}")

