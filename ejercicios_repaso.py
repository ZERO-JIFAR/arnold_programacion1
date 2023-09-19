print("Ejercicio 1")
frase = input("Ingrese una frase: ")
acount_frase = len(frase)
if acount_frase == 4:
    print(frase,"!")
else:
    print(frase,"?")

print("")

print("Ejercicio 2")
import random
list_word=["blanco","azul","negro","rojo","celeste","violeta","verde","rosado","naranja","amarillo"]
print("Adivine la palabra")

acount_try = 5
random_word=random.choice(list_word)
"""
for lett in list_word:
while acount_try>0:
    lett=input("Ingrese una letra: ").upper()

    if 
        acount_try-=1
"""
print()