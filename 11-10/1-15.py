n = input()
nums = list(map(int, input().split(" ")))

cnt = 0

for i in nums:
    print(i, end=" ")
    cnt += 1
    if cnt % 5 == 0:
        print(end="\n")
