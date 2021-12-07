from math import floor
words = input()
origin = words

store = []
flag = True
half_len = floor(len(words) / 2)
if len(words) % 2 != 0:
    words = words[0: half_len] + words[half_len+1:]

for i in range(0, len(words)):
    if i < half_len:
        store.append(words[i])
    elif (i >= half_len):
        poped = store.pop()
        flag = (words[i] == poped)


print(origin, end="")
if not flag:
    print("不", end="")
print("是回文。", end="")