def fun(n):
    a = 0
    b = 1
    i = 0
    l = []
    while i < n:
        l.append(a)
        a, b = a + b, a
        i += 1

    del l[0]
    return l


n = int(input())

for i,val in enumerate(fun(n + 1)):
    if i!= 0:
        print(" ", end="")
    
    print(val, end="")
