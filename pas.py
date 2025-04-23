edad=int(input("\nescribe edad"))
if edad<18:
    print("\nNo puedes pasar eres menor de edad")   
  
elif edad>18:  
    pase=input("\ntienes pase dorado Si/No")
    
    if pase =="si":
         print ("\nPuedes entrar")
    elif pase== "no":
        if edad >= 18 and edad <=25:
            print("\npuedes entrar")
        elif edad >25:
            print("\nno puedes entrar")

        
     
      