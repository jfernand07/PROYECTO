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
# Validación de calificación individual
while True:
    calificacion = input("Ingresa una calificación numérica (0-100): ")
    if calificacion.replace('.', '', 1).isdigit():
        calificacion = float(calificacion)
        if calificacion >= 60:
            print("El estudiante ha aprobado.")
        else:
            print("El estudiante ha reprobado.")
        break  # Salir del bucle una vez que la entrada es válida
    else:
        print("Entrada no válida. Se esperaba un número.")

# Ingreso de calificaciones
calificaciones = []
entrada = input("\nIngresa una lista de calificaciones separadas por comas: ")
for x in entrada.split(","):
    x = x.strip()
    if x.replace('.', '', 1).isdigit(): ## Validación de entrada i usamos el isdigit() para verificar si es un número
        calificaciones.append(float(x))

# Cálculo de promedio
if calificaciones:
    promedio = sum(calificaciones) / len(calificaciones)
    print(f"\nEl promedio de las calificaciones es: {promedio:.2f}")

    # Determinar si se aprobó o reprobó
    if promedio >= 60:
        print(f"Ganó con un promedio de {promedio:.2f}")
    else:
        print(f"Perdió con un promedio de {promedio:.2f}")
else:
    print("No se ingresaron calificaciones válidas.")

# Contar calificaciones mayores que un valor
while calificaciones:
    valor = input("\nIngresa un valor para contar cuántas calificaciones son mayores: ")
    if valor.replace('.', '', 1).isdigit(): ## Validación de entrada i usamos el isdigit() para verificar si es un número
        valor = float(valor)
        mayores = 0
        for nota in calificaciones:
            if nota > valor:
                mayores += 1
        print(f"Cantidad de calificaciones mayores que {valor}: {mayores}")
        break  # Salir del bucle tras una entrada válida
    else:
        print("Entrada no válida. Se esperaba un número.")

# Verificar y contar una calificación específica
while calificaciones:
    buscar = input("\nIngresa una calificación específica a buscar en la lista: ")
    if buscar.replace('.', '', 1).isdigit(): ## Validación de entrada i usamos el isdigit() para verificar si es un número
        buscar = float(buscar)
        contador = 0
        for nota in calificaciones:
            if nota == buscar:
                contador += 1
        print(f"La calificación {buscar} aparece {contador} veces en la lista.") if contador else print(f"La calificación {buscar} no está en la lista.")
        break  # Salir del bucle tras una entrada válida
    else:
        print("Entrada no válida. Se esperaba un número.")
