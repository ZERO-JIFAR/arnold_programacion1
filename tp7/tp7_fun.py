
#cargado de datos de la lista de numeros
def list_assem_num():
    list_num0=[]
    while True:
        p=int(input("Ingrese un numero (0 para salir): "))
        list_num0.append(p)
        if p==0:
            break
    print (list_num0)
    return list_num0

#cargado de datos de la lista de palabras
def list_assem_word():
    list_word0=[]
    while True:
        p=str(input("Ingrese una palabra (vacio para salir): "))
        if p==" ":
            break
        elif p.isalpha():
            list_word0.append(p)
        else:
            print("Ingrese una palabra.")
    print (list_word0)
    return list_word0

#1
def ejer1(list_num1):
    n = len(list_num1)
    for i in range(n-1):
            for j in range(n-1-i):
                if list_num1[j] > list_num1[j+1]:
                    list_num1[j], list_num1[j+1] = list_num1[j+1], list_num1[j]
    return list_num1

#2
def selection_sort_words(list_word2):
    len_word = len(list_word2)
    for i in range(len_word - 1):
        min_index = i
        for j in range(i + 1, len_word):
            if list_word2[j] < list_word2[min_index]:
                min_index = j
        list_word2[i], list_word2[min_index] = list_word2[min_index], list_word2[i]
    return list_word2

#3

#4
def insertionSort(li):
    n = len(li)
    if n <= 1:
        return li
    for i in range(1, n):
        key = li[i]
        j = i-1
        while j >= 0 and len(key) < len(li[j]):
            li[j+1] = li[j]
            j -= 1
        li[j+1] = key

#5
def ejer5(list_num2):
    n = len(list_num2)
    for i in range(n-1):
            for j in range(n-1-i):
                if list_num2[j] < list_num2[j+1]:
                    list_num2[j], list_num2[j+1] = list_num2[j+1], list_num2[j]
    return list_num2

#6
def ejer6(list_num6):
    output = [0 for i in range(len(list_num6))]
    count = [0 for i in range(1000000)]
    for i in list_num6:
        count[i] += 1
    for i in range(1, 1000000):
        count[i] += count[i-1]
    for i in range(len(list_num6)):
        output[count[list_num6[i]]-1] = list_num6[i]
        count[list_num6[i]] -= 1
    return output

#7
def insertionSort(word_list):
    if len(word_list) <= 1:
        return word_list
    else:    
        for i in range(1, len(word_list)):
            key = word_list[i]
            j = i-1
            while j >= 0 and key < word_list[j]:
                word_list[j+1] =  word_list[j]
                j -= 1
            word_list[j+1] = key
        return word_list

def bubbleSort(number_list):
    n = len(number_list)
    swapped = False
    for i in range(n-1):
        for j in range(0, n-i-1):
            if number_list[j] > number_list[j + 1]:
                swapped = True
                number_list[j], number_list[j + 1] = number_list[j + 1], number_list[j]
        if not swapped:
            return number_list
    return number_list

#8
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr