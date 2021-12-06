n = int(input())

nums = list(map(int, input().split(" ")))

sum = 0
fail = 0
for x in nums:
    sum += x
    if x < 60:
        fail += 1
    
print("""Max: {}
Min: {}
Ave: {}
Fail: {}
""".format(max(nums), min(nums), sum/n, fail))