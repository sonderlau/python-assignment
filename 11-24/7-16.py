alpha = list(input().split(" "))
beta = list(input().split(" "))

r = list()

for x in alpha:
    if x not in beta:
        r.append(x)

for x in beta:
    if x not in alpha:
        r.append(x)

for x in r:
    if x != r[0]:
        print(" ", end="")
    print(x, end="")
