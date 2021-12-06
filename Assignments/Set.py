n = input()

nums = map(int, input().split(" "))

nums = set(nums)
sorted(nums)

print(len(nums))
for k, v in enumerate(nums):
    print(v, end="")
    if k != len(nums) - 1:
        print(" ", end="")
