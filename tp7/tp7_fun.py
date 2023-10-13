#1
def ejer1(list_num1):
    n = len(list_num1)
    for i in range(n-1):
            for j in range(n-1-i):
                if list_num1[j] > list_num1[j+1]:
                    list_num1[j], list_num1[j+1] = list_num1[j+1], list_num1[j]
    return list_num1

#5
def ejer5(list_num2):
    n = len(list_num2)
    for i in range(n-1):
            for j in range(n-1-i):
                if list_num2[j] < list_num2[j+1]:
                    list_num2[j], list_num2[j+1] = list_num2[j+1], list_num2[j]
    return list_num2