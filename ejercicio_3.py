#Extraer hora, minuto y segudos
seg=float(input("ingresa un numero en segundos para extraer su hora, minutos y segndos : "))
hora= seg / 3600
Min= (seg / 60) - (round(hora)*60)
segf= seg - (round(Min)*60) - 3600
print ("el tiempo es ", round(hora) ,"horas y",round(Min) ,"minutos con ", round(segf)  ,"segundos",)
