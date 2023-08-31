print("Ejercicio 1")
alfabeto='abcdefghijklmnñopqrstuvwxyzabcd'
for i in range (5):
    x=''
    oracion=input("Ingrese una oracion: ")
    for i in oracion:
        if (i in alfabeto):
            ind=alfabeto.find(i)
            ind+=3%27
            x+=alfabeto[ind]
        else:
            x+=i
    print(x)

print("")

print("Ejercicio 2")
digito_par = 0
digito_impar = 0
contador_par = 0
contador_impar = 0
num_ingresado = int(input("Ingresá un numero entero positivo: "))
while num_ingresado != 0:
    num_aux  = num_ingresado
    while num_aux>=1:
        resto = num_aux%10   
        num_aux = int(num_aux/10)
        if resto % 2 == 0:
            digito_par += 1
            contador_par += 1
        else:
            digito_impar += 1
            contador_impar +=1
    print("Este numero tiene", digito_par, "digitos pares y", digito_impar,"digitos impares.")
    digito_par = 0
    digito_impar = 0
    print("")
    num_ingresado = int(input("Ingresá otro numero entero positivo: "))
print("Numeros pares ingresados:", contador_par)
print("Numeros impares ingresados:", contador_impar)