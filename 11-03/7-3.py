def check_length(num):
    return len(num) <= 5


def check_prime(num):
    x = int(num)
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


def check_symmetrical(s):
    return list(s) == list(reversed(s))


while True:
    try:
        num = input()
        if check_length(num) and check_prime(num) and check_symmetrical(num):
            print("Yes")
        else:
            print("No")
    except:
        break
