def ok(shrink, release):
    return shrink >= 90 and shrink <= 140 and release >= 60 and release <= 90

n = int(input())

cnt = 0
for i in range(0, n):
    nums = list(map(int, input().split(" ")))
    if ok(nums[0],nums[1]):
        print(nums)
        cnt += 1
    
print(cnt - 1)
    