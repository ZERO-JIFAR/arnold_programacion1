import tp7_fun

list_num=tp7_fun.list_assem_num()
list_word=tp7_fun.list_assem_word()

print("")

print("Ejercicio 1.")
print("Ordenamiento de burbuja (ascendente)")
list_num1=list_num.copy()
print(tp7_fun.ejer1(list_num1))

print("")

print("Ejercicio 2")
print("Ordenamiento de selección")
list_word2=list_word.copy()
print("Palabras ordenadas alfabéticamente:", tp7_fun.selection_sort_words(list_word2))

print("")

print("Ejercicio 3.")
books = [
    {"titulo": "Yo Robot", "autor": "Isaac Asimov", "año": 1950},
    {"titulo": "Dune", "autor": "Frank Herbert", "año": 1965},
    {"titulo": "Veinte Mil Leguas de Viaje Submarino", "autor": "Julio Verne", "año": 1870},
    {"titulo": "It", "autor": "Stephen King", "año": 1986}
]
parameter = input("Ingrese el parámetro de ordenamiento (titulo/autor/año): ").lower()
if parameter not in ["titulo", "autor", "año"]:
    print("Parámetro no válido. Debe ser 'titulo', 'autor' o 'año'.")
else:
    ordered_books = sorted(books, key=lambda x: x[parameter])
    print("Libros ordenados por", parameter)
    for book in ordered_books:
        print(f"Título: {book['titulo']}, Autor: {book['autor']}, Año: {book['año']}")

print("")

print("Ejercicio 4.")
print("Ordenamiento de inserción")
list_word4=list_word.copy()
print("Palabras ordenadas en orden ascendente segun su longitud:",tp7_fun.ejer4(list_word4))

print("")

print("Ejercicio 5.")
print("Ordenamiento de burbuja (descendente)")
list_num5=list_num.copy()
print(tp7_fun.ejer5(list_num5))

print("")

print("Ejercicio 6.")
print("Ordenamiento por conteo")
list_num6=list_num.copy()
print(tp7_fun.ejer6(list_num6))

print("")

print("Ejercicio 7")
words_and_numbers = []
words =[]
numbers = []
while True:
    list_input = input("Ingrese numeros y palabras (0 para salir): ").lower()
    if list_input == '0':
        break
    else:
        words_and_numbers.append(list_input)
for element in words_and_numbers:
    if element.isalpha():
        words.append(element)
    else:
        numbers.append(int(element))
words_and_numbers = tp7_fun.bubbleSort(numbers) + tp7_fun.insertionSort(words)
print("Números ordenados de menor a mayor y cadenas ordenadas alfabéticamente: ", words_and_numbers)

print("")

print("Ejercicio 8")
print("Ordenamiento Merge Sort")
list_num8=list_num.copy()
print(tp7_fun.merge_sort(list_num8))
