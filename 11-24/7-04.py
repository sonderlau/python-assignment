s = list(map(int, input().split(",")))
n = []
for i in range(1, 6):
    if s.count(i) == 0:
        n.append(str(i))
m = []
for i in range(6, 11):
    if s.count(i) == 0:
        m.append(str(i))

print(" ".join(n))
print(" ".join(m))
