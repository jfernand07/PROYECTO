precio=float(input("Ingrese el valor a pagar: "))
propina=int(input("Ingrese la propina(10,15,20): "))

print(f"Su pago total es: {precio+(precio*(propina/100))}")