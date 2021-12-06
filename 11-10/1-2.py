words = input().split(" ")
max = 0

for i, val in enumerate(words):
    if len(val) > len(words[max]):
        max = i

print(words[max])
