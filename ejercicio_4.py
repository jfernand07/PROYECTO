#Fecha Formateada

try: 
    dia=int(input("ingresa dia"))
    mes=int(input("ingresa mes"))
    año=int(input("ingresa año"))
    print (dia,"/",mes,"/",año)
except ValueError: 
    print ("solo numero enteros")