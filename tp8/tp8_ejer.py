import tp8_fun

print("Ejercicio 1.")
num=int(input("Ingrese un numero: "))
print("Cantida de digitos:",tp8_fun.dig(num))

print("")

print("Ejercicio 2")
num_b = int(input("Ingrese un numero entero: "))
num_n = int(input("Ingrese otro numero entero para verificar si es potencia del anterior: "))
result = tp8_fun.num_power(num_b, num_n)
print(result)

print("")

print("Ejercicio 3")
string_a = str(input("Ingrese una frase: "))
string_b = str(input("Ingrese una palabra o letra que se encuentre dentro de la frase: "))
print(tp8_fun.positions_strings(string_a, string_b))

print("")

print("Ejercicio 4")
while True:
    num = int(input("Ingrese un numero natural: "))
    if num<1:
        print("Ingrese un numero natural.")
    else:
        break
if tp8_fun.even(num) == True:
    print ("El numero es par")
else:
    print("El numero es impar")

print("")

print("Ejercicio 5")
numbers_list = []
while True:
    number = int(input('Ingrese numeros enteros a la lista (0 para terminar): '))
    if number == 0:
        break
    else:
        numbers_list.append(number)
print(numbers_list)
position=0
greater_num = 0
print(f'El mayor numero ingresado es {tp8_fun.greater_element(numbers_list,position,greater_num)}')

print("")

print("Ejercicio 6")
numbers_list2 = []
while True:
    number2 = int(input('Ingrese numeros enteros a la lista (0 para terminar): '))
    if number2 == 0:
        break
    else:
        numbers_list2.append(number2)
new_list=[]
print(numbers_list2)
repeat_n_times = int(input('Cuantas veces quiere replicar los elementos de la lista?: '))
size = len(numbers_list2)
tp8_fun.repeat(numbers_list2,repeat_n_times,new_list)
print(new_list)

print("")

print("Ejercicio 7.")
while True:
    n=int(input("Ingrese un numero n: "))
    p=int(input("Ingrese un numero p: "))
    if n>0 and p>0:
        break
    else:
        print("No puede ingresar 0")
print("Resultado:",tp8_fun.mul(n,p))

print("")

print("Ejercicio 8")
row = int(input("Coloque el valor de la fila: "))
column = int(input("Coloque el valor de la columna: "))
result = tp8_fun.pascal(row, column)
print(f"El valor en la fila {row} y la columna {column} es: {result}")

print("")

print("Ejercicio 9")
char_list= []
while True:
    characters = input('Ingrese distintos caracteres (0 para terminar): ')
    if characters == '0':
        break
    else:
        char_list.append(characters)
len_combination = int(input('Ingrese la longitud de las cadenas a combinar: '))
print(tp8_fun.combinations(char_list, len_combination))

print("")

print("Ejercicio 10.")
paper = int(input("Ingrese el numero de la hoja: A"))
print("Las medidas de las hojas A",paper,"son:",tp8_fun.sheet(paper))