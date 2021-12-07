nums = input().split(" ")
store = []

for i in nums:
    store.append(int(i))

for i in range(len(store) - 1, -1, -1):
    if store[i] == max(store):
        print(max(store), i)
        break
