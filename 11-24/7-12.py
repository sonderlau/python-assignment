nums = set(map(int, input().split(" ")))

sum = 0
for x in nums:
    sum += x

print("{:.3f}".format(sum / len(nums)))