#todas las operaciones
numb1 = int(input("Introduce el primer número: "))
numb2 = int(input("Introduce el segundo número: "))
opera= input("Introduce la operación deseada: +, -, *, /, //, %: ")
if opera == "+":
    print("La suma es: ", numb1 + numb2)
elif opera == "-":
    print("La resta es: ", numb1 - numb2)
elif opera == "*":
    print("La multiplicación es: ", numb1 * numb2)
elif opera == "/": 
    if numb2 != 0:
        print("La división es: ", numb1 / numb2)
    else:
        print("No se puede dividir entre cero")
elif opera == "//":
    if numb2 != 0:
        print("La división entera es: ", numb1 // numb2)
    else:
        print("No se puede dividir entre cero")
elif opera == "%":
    if numb2 != 0:
        print("El módulo es: ", numb1 % numb2)
    else:
        print("No se puede dividir entre cero")
