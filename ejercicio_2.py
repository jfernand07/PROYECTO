numero = input("Introduce un número de tres cifras: ")

centenas = int(numero[0])
decenas = int(numero[1])
unidades = int(numero[2])

numero_inverso = str(unidades) + str(decenas) + str(centenas)

print("El número original es:", numero)
print("El número inverso es:", numero_inverso)