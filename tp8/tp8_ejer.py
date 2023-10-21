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
string_a = "Hola que tal como estas"
string_b = "a"
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

print("")

print("Ejercicio 6")
numbers_list = [1,2,3,4,5,6,7]
new_list=[]
print(numbers_list)
repeat_n_times = int(input('Cuantas veces quiere replicar los elementos de la lista?: '))
size = len(numbers_list)
tp8_fun.repeat(numbers_list,repeat_n_times,new_list)
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

print("")

print("Ejercicio 9")

print("")

print("Ejercicio 10.")
paper = int(input("Ingrese el numero de la hoja: A"))
print("Las medidas de las hojas A",paper,"son:",tp8_fun.sheet(paper))