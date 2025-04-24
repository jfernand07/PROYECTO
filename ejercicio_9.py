#Extraer Dias,hora y minuto
min=float(input("ingresa un numero en Minutos para extraer su informacion en dias, Horas y minutos : "))
dia= min / 1440
hora= (min / 60) - (round(dia)*24)
minf= min - (round(hora)*60) - 1440
minf1= minf / 60
print ("el tiempo es ", round(dia) ,"dias y",round(hora) ,"hora con ", round(minf1)  ,"minutos",)
