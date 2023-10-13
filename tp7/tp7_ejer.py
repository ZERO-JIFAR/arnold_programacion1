import tp7_fun

list_num=[]
while True:
    p=int(input("Ingrese un numero (0 para salir): "))
    list_num.append(p)
    if p==0:
        break
print (list_num)

#1
list_num1=list_num.copy()
print(tp7_fun.ejer1(list_num1))

#5
list_num2=list_num.copy()
print(tp7_fun.ejer5(list_num2))

#6
output = [0 for i in range(len(list_num))]
count = [0 for i in range(10)]
for i in list_num:
    count[i] += 1
for i in range(1, 10):
    count[i] += count[i-1]
for i in range(len(list_num)):
    output[count[list_num[i]]-1] = list_num[i]
    count[list_num[i]] -= 1
print(output)


def countSort(arr):
    output = [0 for i in range(len(arr))]
    count = [0 for i in range(10)]
    for i in arr:
        count[i] += 1
    for i in range(1, 10):
        count[i] += count[i-1]
    for i in range(len(arr)):
        output[count[arr[i]]-1] = arr[i]
        count[arr[i]] -= 1
    return output
arr = [1, 4, 1, 2, 7, 5, 2]
ans = countSort(arr)
print(ans)