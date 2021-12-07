n = int(input())

nums = [i for i in range(1, n + 1)]

nums.append(nums[0])
del nums[0]

print(nums)
