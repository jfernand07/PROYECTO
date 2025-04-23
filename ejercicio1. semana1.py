# Intercambio de Variable
numb1=int(input("ingresa un numero"))
numb2=int(input("ingresa segundo numero"))
print ("numero A es igual a ",numb1 , "Numero B es igual a ",numb2)

#Extraer hora, minuto y segudos
seg=float(input("ingresa un numero en segundos para extraer su hora, minutos y segndos : "))
Min= seg / 60
hora= Min / 60
segf= seg / (hora+Min)
print (f"el tiempo es ", {round(hora, 2)} ,"horas y",{round(Min, 2)} ,"minutos con ", {round(segf, 2)}  ,"segundos",)

#Fecha Formateada

try: 
    dia=int(input("ingresa dia"))
    mes=int(input("ingresa mes"))
    año=int(input("ingresa año"))
    print (dia,"/",mes,"/",año)
except ValueError: 
    print ("solo numero enteros")
    
    
#temperatura en F
    
