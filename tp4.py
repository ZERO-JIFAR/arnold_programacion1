print("Ejercicio 1")
x = 0
exit = 0
while x <= 30:
    if x == 4 or x == 6  or x == 10:
        print('The value ' + str(x) + ' of x was skipped')
    else:
        print('The value of the loop is: ' + str(x))
    x += 1
    if x == 15:
        print('The execution of the loop was broken when x was ' + str(x))
        break

print("")

print("Ejercicio 1")
line=" "
while line != "":
    line = input("Ingrese una palabra o frase (espacio para salir): ").upper()
    if line == "":
        break
    print(line)

print("")

print("Ejercicio 2")
op = "D"
ac = 0
while op != "D" or op != "R":
    op = input("Presiona D y el monto para ingresar dinero o R y el monto para retirar (espacio para salir): ").upper()
    if op=="":
        break
    elif op[0]== "D":
        split_str = op.split()
        amount = int(split_str[1])
        ac += amount
    elif op[0]== "R":
        split_str = op.split()
        amount = int(split_str[1])
        ac -= amount
    else:
        print("Ingrese una opcion valida")
print("Su saldo es de:",ac)

print("")

print("Ejercicio 3")
num=1
acc=0
while num > 0:
    num = int(input("Ingrese un numero mayor que 1 (0 para salir): "))
    if num == 0:
        break
    elif num%2==0 or num%3==0:
        if num<4:
            acc+=1
        continue
    elif num%num==0:
        acc+=1
print(acc,"numeros primos fueron ingresados")

print("")

print("Ejercicio 4")
year1 = int(input('Ingrese un año: '))
year2 = int(input('Ingrese otro año: '))
if year1<year2:
    print('Año bisiesto y multiplo de 10 entre', year1, 'y', year2, ':')
    for i in range(year1, year2+1):
        if i % 10 != 0:
            continue
        elif i % 4 == 0 and (i % 100 != 0 or i%400==0):
            print(i)
else:
    print('Año bisiesto y multiplo de 10 entre', year2, 'y', year1, ':')
    for i in range(year2, year1+1):
        if i % 10 != 0:
            continue
        elif i % 4 == 0 and (i % 100 != 0 or i%400==0):
            print(i)

print("")

print("Ejercicio 5")
for i in range(1, 20+1):
    if i % 2 != 0:
        continue
    print(i)

print("")

print("Ejercicio 6")
listNum = [8, 55, 25, 548, 456, 89, 55, 33, 78]    
numA = int(input("Ingrese un numero de 0 a 1000 para encontrar: "))
for num in listNum :
    if num == numA :
        print(numA, "pertnece a la lista")
        break
else:
    print(numA,"no pertenece a la lista")

print("")

print("Ejercicio 7")
choice=10
while choice>0:
    print("A donde quiere viajar?: ")
    print("1 - Rusia")
    print("2 - EEUU")
    print("3 - Alemania")
    print("4 - Francia")
    print("0 - salir")
    choice=int(input("Seleccione un destino: "))
    if choice == 0:
        break
    elif choice == 1:
        print("Su proximo destino es Rusia")
        print("")
    elif choice == 2:
        print("Su proximo destino es EEUU")
        print("")
    elif choice == 3:
        print("Su proximo destino es Alemania")
        print("")
    elif choice == 4:
        print("Su proximo destino es Francia")
        print("")
    else:
        print("Ingrese un numero valido")
        print("")