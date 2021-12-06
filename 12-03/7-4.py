tmp = input()

nums = list(map(int, input().split(" ")))

tmp = int(input())

for x in range(0, tmp):
    opt = input()
    
    if opt[0:1] == '0':
        k,d = map(int , opt[2:].split(" "))
        if k > len(nums):
            continue
        nums.insert(k, d)
    else:
        k = int(opt[2:])
        if k <= 0 or k >= len(nums):
            continue
        else:
            nums.remove(nums[k - 1])
    print(nums)
            
for x in nums:
    if x != nums[0]:
        print(" ", end="")
    
    print(x, end="")