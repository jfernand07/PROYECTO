num1=int(input("ingrese un numero:"))
  
if num1 % 3 == 0 and num1 % 5 == 0:
    print ("FizzBuzz")   

elif (num1 % 3) ==0:
    print("Fizz")
    
elif (num1 % 5) ==0:
    print("Buzz") 
    
else:
    print(num1)
    
