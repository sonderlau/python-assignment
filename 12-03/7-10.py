import random

n = int(input())

origin = [x for x in range(1, n + 1)]

print(origin)

random.seed(n)

m = random.randint(1, n - 1)

for g in origin:
    if g % m == 0:
        origin.remove(g)

print(origin)
