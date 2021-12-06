l = list([12,3,48,6,79,63,89,7])

print("列表逆序结果为：[", end="")
for i in range(len(l) - 1, -1 , -1):
    if i != l[-1]:
        print(", ", end="")
    print(l[i], end="")
print("]", end="")
print()

l.sort()
print("列表升序排序结果为：", end="")
print(l)

l.sort(reverse=True)
print("列表降序排序结果为：", end="")
print(l)
    