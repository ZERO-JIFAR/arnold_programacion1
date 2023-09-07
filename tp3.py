print("Ejercicio 1")
word = input("Escribe una palabra: ")
for p in range(10):
    print(p+1,"--",word)

print("")

print("Ejercicio 2")
age=int(input("Ingrese su edad: "))
for i in range (age):
    print("Usted a cumplido:",i+1)

print("")

print("Ejercicio 3")
num = int(input("Ingrese un número positivo: "))
list_num=[]
for num in range(1,num+1,2):
    list_num.append(num)
print(list_num)

print("")

print("Ejercicio 4")
number = int(input("Ingrese un número positivo: "))
for i in range(number, -1, -1):
    if i != 0:
        print(i, end= ",")
    else:
        print(i)

print("")

print("Ejercicio 5")
investment = float(input("Ingrese el monto a invertir: "))
annual_interest = float(input("Ingrese el interes anual: "))
years_amount = int(input("Ingrese la cantidad de años: "))
percent = investment * annual_interest / 100
capital = 0
for i in range(years_amount):
    capital += investment + percent
    print("El capital anual obtenido es:", capital)

print("")

print("Ejercicio 6")
height = int(input("Escribe la altura de un triangulo: "))
triangle = "*"
for i in range(height):
    total = (i+1) * triangle
    print(total)

print("")

print("Ejercicio 7")
for i in range (10):
    print("")
    for j in range (10):
        print((i+1),"X",(j+1),"=",(i+1)*(j+1))

print("")

print("Ejercicio 8")
number = int(input("Ingrese la altura del triangulo: "))
for i in range(1, number+1, 2):
    for j in range(i,0,-2):
        print(j, end=" ")
    print("")

print("")

print("Ejercicio 9")
password="contraseña" 
password2=input("Ingrese su contraseña: ")
while password != password2:
    print("Acceso denegado")
    password2=input("Ingrese su contraseña: ")
if password == password2:
    print("Acceso autorizado")

print("")

print("Ejercicio 10")
number = int(input("Ingrese un numero entero: "))
counter = 0
for i in range(1,number+1):
    if number % i == 0:
        counter+=1
if counter==2 and number!=2:
    print("Es un numero primo")
else:
    print("NO es un numero primo")

print("")

print("Ejercicio 11")
word = input("Escribe una palabra: ")
for i in range(len(word) -1 , -1 , -1):
    print(word[i])

print("")

print("Ejercicio 12")
word = input("Escribe una frase: ")
letter = input("Escribe una letra: ")
counter = 0
for l in word:
    if (l == letter ):
        counter+= 1
print("La letra",letter,"aparece", counter)

print("")

print("Ejercicio 13")
message = print("Ingrese una palabra o una frase para leer el eco. Escriba salir para terminar.")
while message != 'salir':
    phrase=input("Frase o palabra: ")
    if phrase == 'salir':
        break
    print(phrase)

print("")

print("Ejercicio 14")
num1 = input("Escribe un numero entero: ")
num2 = input("Escribe un numero entero: ")
even = 0
odd = 0
for n in num1:
    num = int(n)
    if (num % 2 == 0):
        even += 1
    else:
        odd+=1
print("El primer numero tiene", even, "numeros pares y",odd, "impares")
even = 0
odd = 0
for n in num2:
    num = int(n)
    if (num % 2 == 0):
        even += 1
    else:
        odd+=1
print("El segundo numero tiene", even, "numeros pares y",odd, "impares")

print("")

print("Ejercicio 15")
number = int(input("Ingrese un numero mayor que 0 para ver sus divisores: "))
for i in range(1,number+1):
    if number % i == 0:
        print("Es divisible por", i)

print("")

print("Ejercicio 16")
cantidad_numeros = int(input("Coloque la cantidad de números a ingresar: "))
numeros_conjunto = []
negativo = 0
for i in range(cantidad_numeros):
    numeros = int(input("Coloque los números: "))
    numeros_conjunto.append(numeros)
    if numeros < 0:
        negativo = negativo + 1
print("La cantidad de números negativos ingresados son:", negativo)

print("")

print("Ejercicio 17")
phrase = input("Ingrese una palabra o frase para saber que vocales tiene: ").lower()
vowels = 'aeiou'
for i in vowels:
    vowel_count = phrase.count(i)
    if vowel_count > 0:
        print('Contiene', i)

print("")

print("Ejercicio 18")
fib = [0,1]
for i in range(15): 
    fib.append(fib[-1]+fib[-2])
print(fib)

print("")

print("Ejercicio 19")
savings = float(input("Ingrese el monto que quiere llegar a ahorrar: "))
money = 0
while money < savings:
    money_to_save = float(input("Ingrese dinero a la caja de ahorro: "))
    if money_to_save>0:
        money += money_to_save
    else:
        print("Ingrese un monto válido")
print("Lograste igualar o superar el monto deseado, ahorraste $",money)

print("")

print("Ejercicio 20")
num = int(input("Escribe un numero (0 para finalizar): "))
number_sum = num
while num > 0 :
    num = int(input("Escribe un numero (0 para finalizar): "))
    number_sum += num        
print("La suma de todos los numeros ingresados es: ",number_sum)

print("")

print("Ejercicio 21")
num = int(input("Escribe un numero (0 para finalizar): "))
numHigh = num
while num > 0 :
    num = int(input("Escribe un numero (0 para finalizar): "))
    if (num > numHigh):
        numHigh = num
print("El numero mayor es:",numHigh)

print("")

print("Ejercicio 22")
number = int(input('Ingrese un numero entero positivo o -1 para salir: '))
even_number=0
while (number!=-1):
    sum=0
    string_number = str(number)
    for i in string_number:
        num = int(i)
        sum +=num
    print("La sumatoria de los digitos es:", sum)
    if (number%2 == 0):
        even_number+=1
    number = int(input('Ingrese un numero entero positivo o -1 para salir: '))
print("La cantidad de numeros pares ingresados es:", even_number)

print("")

print("Ejercicio 23")
purchases = []
while True:
    amount = float(input("Ingresa el monto (0 para finalizar): "))
    if amount == 0:
        break 
    else:
        purchases.append(amount)  
total_purchases = sum(purchases)
print("Montos de compra: ")
for amount in purchases:
    print(f"${amount:.2f}")
print(f"Total: ${total_purchases:.2f}")

print("")

print("Ejercicio 24")
purchases = []
while True:
    amount = float(input("Ingresa el monto (0 para finalizar): "))
    if amount == 0:
        break 
    elif amount < 0:
        print("Ingreso invalido")
    else:
        purchases.append(amount)  
total_purchases = sum(purchases)
discount = 0
if total_purchases > 1000:
    discount = total_purchases * 0.10
final_total = total_purchases - discount
print("Montos de compra:")
for amount in purchases:
    print(f"${amount:.2f}")
if discount > 0:
    print(f"Total sin 10% descuento: ${total_purchases:.2f}")
    print(f"Descuento aplicado: ${discount:.2f}")
    print(f"Total a pagar: ${final_total:.2f}")
else:
    print(f"Total: ${total_purchases:.2f}")

print("")

print("Ejercicio 25")
num = int(input("Ingresa un número entero positivo: "))
factorial = 1
if num < 0:
    print("El factorial no está definido para números negativos.")
elif num == 0:
    print("El factorial de 0 es 1.")
else:
    for i in range(1, num + 1):
        factorial *= i
    print(f"El factorial de {num} es {factorial}.")