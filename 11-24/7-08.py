import collections
from icecream import ic

store = collections.defaultdict(lambda: -1)
while True:
    value = list(input().split(":"))
    if len(value) != 2:
        break
    ic(value)
    store[value[0]] = int(value[1])


lesson = input("请输入要查询的课程：")
print()
if store[lesson] == -1:
    print("没有该门课程")
else:
    print(store[lesson])
