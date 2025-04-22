NombreP=str(input("\ningrese el nombre del producto: "))
PrecioUn=float(input("ingrese el precio: "))
if PrecioUn<=0:
    precioUn=float(input("\ningrese el precio: "))
cantidadP= int(input("ingrese la cantidad: "))
if cantidadP<=0:
    cantidadP= int(input("\ningrese la cantidad: ")) 
descuentoP= float(input("ingrese el porcentaje de descuento: "))
if descuentoP<=0 or descuentoP > 100:
    descuentoP= float(input("\ningrese el porcentaje de descuento: "))
elif descuentoP == 0:  
    print("\nNo se aplica descuento.")
totalUn = PrecioUn * cantidadP
totalDes = totalUn * (descuentoP / 100)
totalPago= totalUn - totalDes

print(f"\nNombre del producto: {NombreP}")
print(f"El precio total es: {totalUn}")
print(f"El total valor de descuento es: {totalDes:.2f}")
print(f"Valor total a pagar es: {totalPago}")
