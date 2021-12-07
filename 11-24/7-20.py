raw = input()

raw = raw[1:-1]

r = list(map(int, raw.split(",")))

r.sort(reverse=True)

max = r[0]

min = max

for x in range(0, len(r)):
    if r[x] != min:
        min = r[x]
        break

print("max={}, smax={}".format(max, min))
