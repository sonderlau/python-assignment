import math

a = int(input())
b = int(input())
c = int(input())

legal = True if a + b > c and a + c > b and b + c > a else False

if not legal:
    print("数据错误")
else:
    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print("{:.2f}".format(area))
