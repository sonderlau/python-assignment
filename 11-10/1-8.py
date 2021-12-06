def jc(n):
    sum = 1
    for i in range(1, n + 1):
        sum = sum * i
    return sum


n = int(input())
result = 1
for i in range(1, n + 1):
    result = result + 1 / jc(i)

print("{:.10f}".format(result))
