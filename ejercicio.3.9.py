# Evaluación para tarjeta de crédito

# Solicitar ingresos mensuales
ingresos = float(input("Ingrese sus ingresos mensuales: "))

# Solicitar si tiene deudas activas
tiene_deudas = input("¿Tiene deudas activas? (sí/no): ").strip().lower()

# Evaluar si puede recibir la tarjeta
if ingresos > 2500 or (ingresos > 1500 and tiene_deudas == "no"):
    print("Puede recibir la tarjeta de crédito.")
else:
    print("No puede recibir la tarjeta de crédito.")