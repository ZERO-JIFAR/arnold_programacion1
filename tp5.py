import math

"""
#2
def leng_last_word(chain):
    # Eliminar espacios en blanco al principio y al final de la cadena
    chain = chain.strip()
    
    # Dividir la cadena en palabras usando espacios como delimitador
    word = chain.split()
    # Verificar si hay palabras en la cadena
    if word:
        # La última palabra se encuentra en la última posición de la lista
        last_word = word[-1]
        # Retornar la longitud de la última palabra
        return len(last_word)
    else:
        # Si no hay palabras, retornar 0
        return 0
# Ejemplo de uso
chain = str(input("Ingrse una frase: "))
result = leng_last_word(chain)
print("Longitud de la última palabra:", result)

#8
def calculo_perim(n):
    perimetro=2*n*math.pi
    return perimetro
def calculo_area(n):
    area=(math.pi*n)**2
    return area
radio=float(input("Ingrese el radio del circulo: "))
perimetro=calculo_perim(radio)
area=calculo_area(radio)
print("Perimetro:",perimetro)
print("Area:",area)
"""
#11
def multiplos1(num1):
    
num1=int(input("Ingrese un numero: "))
num2=int(input("Ingrese otro numero: "))
list=[1,2,3,4,5,6,7,8,9]
multiplos1=multiplos_num1(num1)
multiplos2=multiplos_num2(num2)