
#1
def time(n):
    if n == 1:
        return 3
    else:
        return 2 + time(n-1)

#2
def f(n):
    n=str(n)
    if len(n)<=1:
        return n
    return n[-1] + f(int(n[:-1]))