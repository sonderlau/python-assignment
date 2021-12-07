while True:
    try:
        raw = list(input().split(" "))

        nums = list(map(int, raw[2:]))

        nums.append(int(raw[1]))

        nums.sort()

        for x in nums:
            if x != nums[0]:
                print(" ", end="")
            print(x, end="")
        print()
    except EOFError:
        break
