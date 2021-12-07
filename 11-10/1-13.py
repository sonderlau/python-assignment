from icecream import ic

n = int(input())
tmp = 0


def is_prime(x):
    if x == 1:
        return False
    if (x == 2) or (x == 3):
        return True
    if (x % 6 != 1) and (x % 6 != 5):
        return False
    for i in range(5, int(x ** 0.5) + 1, 6):
        if (x % i == 0) or (x % (i + 2) == 0):
            return False
    return True


factors = [set() for x in range(100010)]


# n round
for i in range(0, n):
    tmp = input()
    nums = list(map(int, input().split(" ")))
    one_index = 0
    cnt = 0

    # find 1
    for k, v in enumerate(nums):
        if v == 1:
            one_index = k
            del nums[k]

    # from n to 1

    for x in range(len(nums) - 1, -1, -1):
        visited = [False for n in range(len(nums) + 1)]

        if x < one_index and (one_index + x != 0):
            cnt += 1
            ic("oneindex", cnt, x, one_index)
        if is_prime(nums[x]):
            visited[x] = True
            continue
        else:
            # 后面的
            buffer = set()
            for y in range(len(nums) - 1, x, -1):

                if visited[y]:
                    continue

                if nums[x] % nums[y] == 0:
                    # 这个数 + 这个数的因子个数
                    cnt += 1 + len(factors[nums[y]])

                    factors[nums[x]].add(nums[y])
                    buffer.add(y)
                    visited[y] = True

                ic(nums[x], nums[y], cnt, visited)

                ic(buffer)
                while len(buffer) != 0:
                    f = buffer.pop()
                    visited[f] = True
                    cnt += len(factors[f])
                    buffer.union(factors[f])

    print(cnt)
