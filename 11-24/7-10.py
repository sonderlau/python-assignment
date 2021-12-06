import collections
store = collections.defaultdict(lambda: 0 ) 
n = int(input())

for i in range(0, n):
    raw = list(input().split(":"))
    for match in raw[1].split(","):
        score = list(map(int, match.split("-")))
        value = score[0] - score[1]
        if value >= 2:
            value = 3
        elif value == 1:
            value = 2
        elif value <= -2:
            value = 0
        else:
            value = 1
        store[raw[0]] += value
result = sorted(store.items(), key=lambda x: x[1], reverse=True)
for k in result:
    print("{} : {}".format(k[0], k[1]))