print("Ejercicio 1")
base=float(input("Ingrese la base: "))
altura=float(input("Ingrese la altura: "))
area = base * altura
print("Area:", area )

print("")

print("Ejercicio 2")
a=float(input("Ingrese un numero: "))**2
b=float(input("Ingrese otro numero: "))**2
h=(a+b)**0.5
print("Hipotenusa:",h)

print("")

print("Ejercicio 3")
num1=float(input("Ingrese un numero: "))
num2=float(input("Ingrese otro numero: "))
suma = num1 + num2
resta = num1 - num2
division = num1 / num2
multiplicacion = num1 * num2
print("Suma:", suma )
print("Resta:", resta )
print("Division:", division )
print("Multiplicacion:", multiplicacion )

print("")

print("Ejercicio 4")
grados_fahrenheit = float(input("Ingrese la temperatura en grados Fahrenheit: "))
conversor_temperatura = (grados_fahrenheit - 32) * 5/ 9
print("Temperatura en grados Celsius:",conversor_temperatura) 

print("")

print("Ejercicio 5")
# a) Para guardar el nombre de la canción en la variable esta no debe estar dentro del input.
nombre = input('¿Cuál es tu canción favorita? ')
print(nombre)
# b) Tenemos que transformar el tipo de la variable precio de string a int o float, ya que input nos devuelve una variable de tipo string.
precio = float(input('Precio: '))
total = precio + (precio * 0.1)
print(total)
# c) Cuando queremos imprimir algo que no sea una variable debe ir entre comillas.
edad = int(input('Edad: '))
print('Tu edad es:', edad)
# d) El valor de la variable edad es asignado con el input, y no podemos darle un nuevo valor dentro del print.
edad = int(input('Edad: '))
print('Veamos si tu edad es 18…', edad)

print("")

print("Ejercicio 6")
num1 = float(input('Ingrese el primer numero: '))
num2 = float(input('Ingrese el segundo numero: '))
num3 = float(input('Ingrese el tercer numero: '))
promedio = (num1 + num2 + num3) / 3
print('El promedio de los numeros ingresados es: ', promedio)

print("")

print("Ejercicio 7")
min = int(input("Ingresar una cantidad de minutos: "))
cant_h = min/60
cant_min = min % 60
print("Son", int(cant_h), "horas y",cant_min, "minutos" )

print("")

print("Ejercicio 8")
sueldo_base = float(input('Ingrese el sueldo base: '))
total= sueldo_base + (sueldo_base * .1 * 3)
print("Su sueldo total es:", total)

print("")

print("Ejercicio 9")
precio_final=float(input("Ingrese el valor total de la compra: $"))
print("Precio con descuento: $",precio_final*0.85)

print("")

print("Ejercicio 10")
parcial1 = float(input("Ingrese la nota del primer parcial: "))
parcial2 = float(input("Ingrese la nota del segundo parcial: "))
parcial3 = float(input("Ingrese la nota del tercer parcial: "))
examen_final = float(input("Ingrese la nota del examen final: "))
trabajo_final = float(input("Ingrese la nota del trabajo final: "))
promedio_parciales = (parcial1 + parcial2 + parcial3) / 3
porcentaje_parciales= promedio_parciales * 0.55
porcentaje_examen_final= examen_final * 0.3
porcentaje_trabajo_final = trabajo_final * 0.15
calificacion_final= porcentaje_parciales + porcentaje_examen_final + porcentaje_trabajo_final
print("La calificación final es de:", calificacion_final)

print("")

print("Ejercicio 11")
num_1 = int(input("Ingrese el primer número: ")) 
num_2 = int(input("Ingrese el segundo número: "))
distancia = abs(num_1 -  num_2)
print("La distancia es:",distancia)

print("")

print("Ejercicio 12")
numero = float(input('Ingrese un numero: '))
raiz_cuadrada = numero**(1/2)
raiz_cubica = numero**(1/3)
print('La raiz cuadrada es:', raiz_cuadrada)
print('La raiz cubica es:', raiz_cubica)

print("")

print("Ejercicio 13")
numero = (input('Ingrese un numero: '))
numero = int(numero[::-1])
print("El numero invertido es:",numero)

print("")

print("Ejercicio 14")
a = input("Ingrese el valor de A: ")
b = input("Ingrese el valor de B: ")
c = a
a = b
b = c
print("Ahora A vale:", a, "y B vale:", b )

print("")

print("Ejercicio 15")
hora_partida = int(input("Hora de partida (HH): "))
minuto_partida = int(input("Minuto de partida (MM): "))
segundo_partida = int(input("Segundo de partida (SS): "))
tiempo_viaje = int(input("Tiempo de viaje (T segundos): "))
tiempo_partida_en_segundos = hora_partida * 3600 + minuto_partida * 60 + segundo_partida
tiempo_llegada_en_segundos = tiempo_partida_en_segundos + tiempo_viaje
hh_llegada = tiempo_llegada_en_segundos // 3600
tiempo_llegada_en_segundos %= 3600
mm_llegada = tiempo_llegada_en_segundos // 60
ss_llegada = tiempo_llegada_en_segundos % 60
print("Hora de llegada:", hh_llegada, ":", mm_llegada, ":", ss_llegada)

print("")

print("Ejercicio 16")
nombre = input("Ingrese su nombre: ")
apellido1 = input("Ingrese su primer apellido: ")
apellido2 = input("Ingrese su segundo apellido: ")
print("Iniciales:", nombre[0], apellido1[0], apellido2[0])

print("")

print("Ejercicio 17")
usuario = input('Ingrese su nombre: ')
print('Ahora estas en la matrix', usuario)

print("")

print("Ejercicio 18")
cena = float(input("Ingrese el valor de la cena: "))
total = cena + (cena * 0.062) + (cena * .1)
print("El valor total es:",total)

print("")

print("Ejercicio 19")
fecha = input("Ingrese su día de nacimiento: ")
mes = input("Ingrese su mes de nacimiento: ")
año = input("Ingrese su año de nacimiento: ")
print(fecha, "/", mes, "/", año)

print("")

print("Ejercicio 20")
fecha_nac = int(input('Ingrese su dia de nacimiento: ') 
                + input('Ingrese su mes de nacimiento: ')
                + input('Ingrese su año de nacimiento: '))
print(fecha_nac)

print("")

print("Ejercicio 21")
km_por_litro = float(input("Ingresar kilómetros recorridos por litro de combustible: "))
capacidad_tanque = float(input("Ingresar cantidad de litros que posee el tanque: "))
km_totales = float(input("Ingresar km totales que se van a recorrer: "))
tanques_necesarios = km_totales / km_por_litro / capacidad_tanque
print ("Son necesarios",tanques_necesarios, "tanques de combustible para realizar el viaje")