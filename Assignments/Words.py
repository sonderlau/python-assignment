from collections import defaultdict

store = defaultdict(lambda: 0)
cnt = 0
while True:
    raw = input()
    if raw == "!!!!!":
        break

    for x in list(raw.split(" ")):
        store[x] += 1
        cnt += 1

print(cnt)

round = min(len(store), cnt)
cnt = 0
store = sorted(store.items(), key=lambda x: x[0])


for k in store:
    if cnt == round:
        break
    print(k[0])
    cnt += 1
