m, n = map(int, input().split(" "))

sum = 0
for i in range(m, n + 1):
    sum += i

print("sum = {}".format(sum))
