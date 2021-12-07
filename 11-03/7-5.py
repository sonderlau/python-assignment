nums = map(int, input().split(" "))

nums = list(nums)
del nums[0]

print(max(nums))
