nums = list(map(int, input().split(",")))

max_v = max(nums)

for i, val in enumerate(nums):
    if val == max_v:
        print(i)
