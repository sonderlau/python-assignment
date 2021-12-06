nums = list(map(int, input().split(" ")))   
sum = 0
for x in nums:
    sum += x

print("{} {} {}".format(int(sum / len(nums)), max(nums), min(nums)))