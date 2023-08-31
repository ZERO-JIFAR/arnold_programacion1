#1
word = input("escribe una palabra: ")
for p in range(10):
    print(p+1,"--",word)

#2
age=int(input("Ingrese su edad: "))
for i in range (age):
    print("Usted a cumplido:",i+1)

#4
num_int = int(input("Ingrese un nùmero positivo"))
for num_int in range(num_int, -1, -1):
    print(str(num_int) + ", ")

#6
height = int(input("Escribe la altura de un triangulo: "))
triangle = "*"
for i in range(height):
    total = (i+1) * triangle
    print(total)

#7
for i in range (10):
    print("")
    for j in range (10):
        print((i+1),"X",(j+1),"=",(i+1)*(j+1))

#9
password="contraseña" 
password2=input("Ingrese su contraseña: ")
while password != password2:
    print("Acceso denegado")
    password2=input("Ingrese su contraseña: ")
    if password == password2:
        print("Acceso autorizado")

#11
word = input("escribe una palabra: ")

for i in range(len(word) -1 , -1 , -1):
    print(word[i])

#12
word = input("escribe una frase: ")
letter = input("escribe una letra: ")
counter = 0
for l in word:
    if (l == letter ):
        counter+= 1
print("la letra ",letter," aparece ", counter)

#14
num1 = input("escribe un numero entero: ")
num2 = input("escribe un numero entero: ")
even = 0
odd = 0
for n in num1:
    num = int(n)
    if (num % 2 == 0):
        even += 1
    else:
        odd+=1
print("el primer nuemro tiene ", even, " numeros pares y ",odd, " impares")
even = 0
odd = 0
for n in num2:
    num = int(n)
    if (num % 2 == 0):
        even += 1
    else:
        odd+=1
print("el segundo nuemro tiene ", even, " numeros pares y ",odd, " impares")

#16
cantidad_numeros = int(input("Coloque la cantidad de números a ingresar "))
numeros_conjunto = []
negativo = 0
for i in range(cantidad_numeros):
    numeros = int(input("Coloque los números "))
    numeros_conjunto.append(numeros)
    if numeros < 0:
        negativo = negativo + 1
print("la cantidad de números negativos ingresados son: ", negativo)

#18
fib = [0,1]
for i in range(15): 
    fib.append(fib[-1]+fib[-2])
print(fib)

#21
num = int(input("escribe un numero"))
numHigh = num
while num > 0 :
    num = int(input("escribe un numero"))
    if (num > numHigh):
        numHigh = num
print("el numero mayor es ",numHigh)

