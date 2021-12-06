nums = list(map(int, input().split(" ")))
print(nums)
print(set(nums))
flag = len(set(nums)) == len(list(nums))

if flag:
    print("no")
else:
    print("yes")
