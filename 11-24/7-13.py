nums = list(map(float, input().split(" ")))

for x in nums:
    if x < 5000:
        x = x * 1.5
        if x % 1 == 0:
            print("{:.1f}".format(x), end="")
        else:
            print(x, end="")
    else:
        if x % 1 == 0:
            x = int(x)
        print(x, end="")

    if x != nums[-1]:
        print(" ", end="")
