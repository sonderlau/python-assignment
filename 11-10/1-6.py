raw = input()
raw = raw[1:-1]

s = raw.split(",")

index = set(s)

new_location = dict(zip(index, [0 for x in range(0, len(index))]))

for i, val in enumerate(s):
    new_location[val] = i


sort = sorted(new_location.items(), key=lambda kv: kv[1])


result = []
for key in sort:

    result.append(key[0])

print("[", end="")
for i, val in enumerate(result):
    if i != 0:
        print(", ", end="")
    print(val, end="")
print("]", end="")
