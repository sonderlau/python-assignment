ls = ["2", "3", "0", "1", "5"]

s = input()

i = int(input())

if i >= 5:
    ls.append(s)
else:
    ls.insert(i, s)

ls.append(s)

print(ls)
