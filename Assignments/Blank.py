s = input()
d = {}
for x in s:
    if x in d:
        d[x] = 0
    else:
        d[x] = 1
c = s[0]
for k in d:
    if d[k] > d[c]:
        c = k
print(c, d[c])
