# Sistema de validacion
#primero pedimos ingresa los valores como nombre, precio, si tiene descuento o no
#definimos las variables de nombre, precio, y descuento
NombreP=str(input("\ningrese el nombre del producto: "))
PrecioUn=float(input("ingrese el precio: "))

# agregamos condiciones como, ingreso de valores tienen que ser mayor a 0 
if PrecioUn<=0:
    precioUn=float(input("\ningrese el precio: "))
cantidadP= int(input("ingrese la cantidad: "))
if cantidadP<=0:
    cantidadP= int(input("\ningrese la cantidad: "))
    
    #agregamos una condicion de respuesta para validar si el producto tiene o no descuento 
    # en caso de no tener descuento pasar directamente a dar la informacion 
    #en caso de que si pasar a hacer la operacion y solicitar la infromacion del porcentaje de descuento
producto= str(input("El producto tiene descuento si/no :"))
if  producto == "si": 
    descuentoP= float(input("ingrese el porcentaje de descuento (10%, 15%, 20%): "))
    if descuentoP<=0 or descuentoP > 100:
            descuentoP= float(input("\ningrese el porcentaje de descuento (10%, 15%, 20%) : "))
elif producto == "no":
    descuentoP= 0         
    #hacemos las operaciones matematicas con las variables definidas
        
totalUn = PrecioUn * cantidadP
totalDes = totalUn * (descuentoP / 100)
totalPago= totalUn - totalDes

#damos la respuesta final del producto con sus respectiva infromacion, precio, descuento, nombre y cantidad

print(f"\nNombre del producto: {NombreP}")
print(f"El precio total es: {totalUn}")
print(f"El total valor de descuento es: {totalDes:.2f}")
print(f"Valor total a pagar es: {totalPago}")
