#Extraer hora, minuto y segudos
seg=float(float("ingresa un numero en segundos para extraer su hora, minutos y segndos : "))
Min= seg % 60
hora= Min % 60
segf= seg % (hora+Min)
print ("el tiempo es ", hora ,"horas y",Min ,"minutos con ", segf  ,"segundos",)
