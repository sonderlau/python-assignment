def prime_number(a, b):
    flag = 0
    for i in range(a, b + 1):
        for j in range(2, i):
            if i % j == 0:
                flag = 1
                break
        if i != 1 and flag == 0:
            print(i)
        else:
            flag = 0


a = int(input())
b = int(input())
prime_number(a, b) if a < b else prime_number(b, a)
