alist = set(map(int, input().split()))
blist = set(map(int, input().split()))


alist.update(blist)

alist = sorted(alist)

print("[", end="")
for k, v in enumerate(alist):
    print(v, end="")
    if k != len(alist) - 1:
        print(", ", end="")
print("]", end="")
