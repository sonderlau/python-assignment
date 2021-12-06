round = int(input())

for i in range(round):
    nums = input().split(" ")
    sum = 0
    for x in nums:
        sum += int(x)
    sum /= len(nums)
    print("{:.1f}".format(sum))

