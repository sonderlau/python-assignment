odd = list()
even = list()

while True:
    try:
        x = input()
        if x == '':
            break
        else:
            x = int(x)
        if x % 2 == 0:
            even.append(x)
        else:
            odd.append(x)
    
    except EOFError:
        break

for y in even:
    if y != even[0]:
        print("-", end="")
    print(y, end="")

print()

for y in odd:
    if y != odd[0]:
        print("+", end="")
    print(y, end="")