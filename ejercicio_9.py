min=float(input("ingrese el tiempo en minutos: "))

horas= min/60
dias= min /1440
minf= min - int(1440*dias)
print("dias : ",round(dias,2), ", horas :" , round(horas,2), ", minutos :", round(minf,2))