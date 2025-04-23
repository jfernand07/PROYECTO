
# Intercambio de Variable
numb1=int(input("ingresa un numero"))
numb2=int(input("ingresa segundo numero"))
print ("numero A es igual a ",numb1 , "Numero B es igual a ",numb2)

#Extraer hora, minuto y segudos
seg=float(input("ingresa un numero en segundos para extraer su hora, minutos y segndos : "))
Min= seg % 60
hora= Min % 60
segf= seg % (hora+Min)
print ("el tiempo es ", hora ,"horas y",Min ,"minutos con ", segf  ,"segundos",)

#Fecha Formateada

try: 
    dia=int(input("ingresa dia"))
    mes=int(input("ingresa mes"))
    año=int(input("ingresa año"))
    print (dia,"/",mes,"/",año)
except ValueError: 
    print ("solo numero enteros")
    
    
#temperatura en F
    
    temp1=int(input("ingrese la temperatura"))
    print("la temperatura es ", temp1 -32 (*0.5556))
    