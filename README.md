def Ingreso_Datos(mensaje):
    # Solicitar al usuario que ingrese un número
    valor = float(input(mensaje))
    if valor < 0:
        # Si el número es negativo, mostrar un mensaje de error y volver a solicitar el número
        print("Por favor, ingresa precio.")
        return Ingreso_Datos(mensaje)
        return valor                        
        except ValueError:
        print("Entrada inválida. Por favor, valor válido.")
    # Validar que el número sea positivo
        return numero

def validar_descuento(mensaje):
        while True:
        try:
        descuento = float(input(mensaje))
        if 0 <= descuento <= 100:
        return descuento
        else:
            # Si el porcentaje no está en el rango válido, mostrar un mensaje de error y volver a solicitar el porcentaje
print("Por favor, ingresa un porcentaje de descuento entre 0 y 100.")
        except ValueError:
print("Entrada inválida. Por favor, ingresa un número válido.")
        
def main():
    print("Bienvenido al programa de cálculo de costo total.")
    
    nombre_producto = input("Ingresa el nombre del producto: ")
    precio_unitario = Ingreso_Datos("Ingresa el precio unitario del producto: ")
    cantidad = Ingreso_Datos("Ingresa la cantidad de productos adquiridos: ")
    porcentaje_descuento = validar_descuento("Ingresa el porcentaje de descuento (0-100): ")

    costo_sin_descuento = precio_unitario * cantidad
    descuento = costo_sin_descuento * (porcentaje_descuento / 100)
    costo_total = costo_sin_descuento - descuento

    print(f"\nProducto: {nombre_producto}")
    print(f"Costo total (con descuento aplicado): ${costo_total:.2f}")  
    if __name__ == "__main__":
        main()
