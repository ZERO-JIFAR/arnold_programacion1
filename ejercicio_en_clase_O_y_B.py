from tp7 import tp7_fun

list_num=tp7_fun.list_assem_num()
list_word=tp7_fun.list_assem_word()

print("Ordenamiento de burbuja")
list_num1=list_num.copy()
print(tp7_fun.ejer1(list_num1))

print("Ordenamiento de selección")
list_word2=list_word.copy()
print("Palabras ordenadas alfabéticamente:", tp7_fun.selection_sort_words(list_word2))

print("Ordenamiento de inserción")
list_word4=list_word.copy()
print("Palabras ordenadas en orden ascendente segun su longitud:",tp7_fun.ejer4(list_word4))

print("Ordenamiento Merge Sort")
list_num8=list_num.copy()
print(tp7_fun.merge_sort(list_num8))

print("Busqueda lineal")
number = int(input("Ingrese el numero a buscar: "))
result = tp7_fun.linear_search(list_num, number)
if result != -1:
    print(f"El elemento {number} se encuentra en el índice {result}.")
else:
    print(f"El elemento {number} no se encuentra en la lista.")

print("Busqueda binaria")
result2 = tp7_fun.binary_search(list_num, number)
if result2 != -1:
    print(f"El elemento {number} se encuentra en el índice {result2}.")
else:
    print(f"El elemento {number} no se encuentra en la lista.")