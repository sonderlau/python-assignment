import collections
import string

a = input()
b = input()

if len(a) != len(b):
    print("False")
    exit()
else:
    diff = list()
    for x in range(0, len(a)):
        if a[x] == b[x]:
            continue
        else:
            diff.append(x)

if len(diff) == 2 and (a[diff[1]] == b[diff[0]] and a[diff[0]] == b[diff[1]]):
    print("True")
elif len(diff) == 0:
    # find the same 2
    s = dict.fromkeys(string.ascii_lowercase, 0)
    for x in a:
        s[x] += 1
    r = sorted(s.items(), key=lambda x: x[1], reverse=True)
    if r[0][1] >= 2:
        print("True")
    else:
        print("False")

else:
    print("False")
