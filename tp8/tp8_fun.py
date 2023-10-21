#1
def dig(num,coun=0):
    while True:
        if num<1:
            if coun==0:
                coun= coun+1
                return coun
            return coun
        else:
            num=num//10
            coun= coun+1
            return dig(num,coun)

#2
def num_power(num_b, num_n):
    if num_n < num_b:
        return False
    if num_n == num_b:
        return True
    if num_n % num_b == 0:
        return num_power(num_b,(num_n//num_b))
    return False

#3
def positions_strings(a, b, start=0, result=None):
    if result is None:
        result = []
    index = a.find(b, start)
    if index != -1:
        result.append(index)
        positions_strings(a, b, index + 1, result)
    return result

#4
def even(num):
    if num == 0:
        return True
    else:
        return odd(num-1)
def odd(num):
    if num == 0:
        return False
    else:
        return even(num-1)

#6
def repeat(li,times,new_li):
    counter=len(li)
    if times==0:
        return new_li.sort()
    else:
        add_elements(li,counter,times,new_li)
def add_elements(li,counter,times,new_li):
    if counter == 0:
        repeat(li,times-1,new_li)
    else:
        element = li[len(li)-counter]
        new_li.append(element)
        add_elements(li,counter-1,times,new_li)

#7
def mul(n,p,res=0):
    while True:
        if n==0:
            return res
        else:
            res=res+(p*n)
            n=n-1
            return mul(n,p,res)

#10
def sheet(paper,a=0,long=841,broad=1189):
    while True:
        if a==paper:
            return long,broad
        else:
            a=a+1
            if a%2==0:
                long=long//2
            else:
                broad=broad//2
            return sheet(paper,a,long,broad)