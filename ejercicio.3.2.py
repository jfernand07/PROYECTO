# Solicitar el monto total de la compra y la edad del cliente
monto_total = float(input("Ingrese el monto total de la compra: "))
edad_cliente = int(input("Ingrese la edad del cliente: "))

# Verificar si el cliente obtiene descuento
if monto_total > 100 or edad_cliente > 60:
    print("¡Felicidades! Usted obtiene un descuento.")
else:
    print("Lo sentimos, no aplica para descuento.")