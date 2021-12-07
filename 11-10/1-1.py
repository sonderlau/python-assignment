nums = list(input().split(" "))

flag = len(list(set(nums))) == len(nums)

if flag:
    print("no")
else:
    print("yes")
