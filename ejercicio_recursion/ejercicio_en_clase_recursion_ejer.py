import random
import ejercicio_en_clase_recursion_fun

print("Ejercicio 1")
total_time = 0
print("¿Que camino elige la rata?")
while True:
    path = random.randint(1,3)
    print(f"La rata eligió el camino {path}.")
    time = ejercicio_en_clase_recursion_fun.time(path)
    print(f"Tiempo: {time} minutos.")
    total_time += time
    if path == 3:
        print(f"A la rata le tomó {total_time} minutos salir de la jaula.")
        break

print("")

print("Ejercicio 2")
print("Ingrese un numero entero. El programa devolvera el numero invertido.")
num = int(input("Ingrese un numero:"))
print(ejercicio_en_clase_recursion_fun.f(num))