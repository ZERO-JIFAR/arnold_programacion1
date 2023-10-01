import tp5_fun

print("Ejercicio 1")
document_num = input("Ingrese su DNI: ")
if ( tp5_fun.document(document_num)):
    print("La longitud es correcta")
else:
    print("La longitud es incorrecta")

print("")

print("Ejercicio 2.")
chain = str(input("Ingrse una frase: "))
result = tp5_fun.leng_last_word(chain)
print("Longitud de la última palabra:", result)

print("")

print("Ejercicio 3")
first_name = input("Ingresar nombre de pila: ")
second_name = input("Ingresar segundo nombre, de no tenerlo ingrese 0: ")
last_name = input("Ingresar apellido: ")
last_name_long = len(last_name)
dni = ""
dni_3_digits = 0
print(tp5_fun.user_name(first_name, second_name, last_name))
dni = input("Ingrese su DNI: ")
while(len(dni) != 7 and len(dni) != 8):
    dni = input("DNI inválido. Ingrese el correcto: ")
dni_3_digits = dni[:3]
final_id = "ID: " + first_name + str(last_name_long) + str(dni_3_digits)
print(final_id)

print("")

print("Ejercicio 4")
number1 = int(input("Ingrese un numero entero: "))
while tp5_fun.data_validation(number1) == False:
    number1 = int(input("Ingrese un numero entero: "))
number2 = int(input("Ingrese otro numero entero: "))
while tp5_fun.data_validation(number2) == False:
    number2 = int(input("Ingrese otro numero entero: "))
tp5_fun.is_multiple(number1,number2)

print("")

print("Ejercicio 5")
days = int(input("de cuantos dias desea saber la temperatura media"))
for day in range(days):
    min_tem = int(input("Cual es la temperatura minima?: "))
    max_tem = int(input("Cual es la temperatura maxima?: "))
    print("la temperatura media es ",tp5_fun.temperature_middle(min_tem, max_tem),"º")

print("")

print("Ejercicio 6")
sentence = input("INGRESE FRASE: ")
print("la frase separada es ",tp5_fun.separator(sentence))

print("")

print("Ejercicio 7")
num=1
numbers_list = []
while num!=0:
    print("Ingrese sucesivamente numeros enteros (0 para terminar).")
    num=int(input("Numero: "))
    numbers_list.append(num)
tp5_fun.max_min(numbers_list)

print("")

print("Ejercicio 8.")
radio=float(input("Ingrese el radio del circulo: "))
perimetro=tp5_fun.calculo_perim(radio)
area=tp5_fun.calculo_area(radio)
print("Perimetro:",perimetro)
print("Area:",area)

print("")

print("Ejercicio 9")

print("")

print("Ejercicio 10")
shopping_cart = {3500: '20%', 14200: '35%', 5700: '10%', 12000: '20%', 7800: '10%'}
print("Su carrito de compras con precio y descuento a aplicar es:")
print(shopping_cart)
while True:
    choise = input("Presione T para ver el total con el descuento aplicado y C para cancelar la compra: ").upper()
    if choise == 'T':
        tp5_fun.total(shopping_cart)
        break
    elif choise == 'C':
        print("Compra cancelada")
        break
    else:
        print("Ingrese una opcion correcta")

print("")

print("Ejercicio 11")
#def multiplos1(num1):
    
#num1=int(input("Ingrese un numero: "))
#num2=int(input("Ingrese otro numero: "))
#list=[1,2,3,4,5,6,7,8,9]
#multiplos1=multiplos_num1(num1)
#multiplos2=multiplos_num2(num2)

print("")

print("Ejercicio 12")

print("")

print("Ejercicio 13")
vector = []
prompt = 1
while (prompt >= 1 and prompt <= 3):
    prompt += 1
    digit = input("Ingrese valor del vector")
    vector.append(digit)
print("El módulo del vector es: " , tp5_fun.vector_module(int(vector[0]), int(vector[1]), int(vector[2])))

print("")

print("Ejercicio 14.")
num=int(input("Ingrese un numero: "))
if tp5_fun.es_primo(num) == True:
    print(num,"es un numero primo")
else:
    print(num,"no es un numero primo")

print("")

print("Ejercicio 15.")
cont=0
while True:
    number=int(input("Ingrese un numero (0 para salir): "))
    cont+=1
    if number == 0:
        print("Has ingresado",cont-1,"numeros")
        break
    else:
        fact5=tp5_fun.factorial(number)
        print("El factorial de",number,"es:",fact5)

print("")

print("Ejercicio 16")
num = int(input("Ingrese un número entero "))
digit = int(input("Ingrese un digito "))
tp5_fun.frecuencia(num, digit)

print("")

print("Ejercicio 17")
