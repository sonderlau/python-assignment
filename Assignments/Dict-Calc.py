opts = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y,
}


def to_num(s: str):
    try:
        return int(s)
    except ValueError:
        return float(s)


a = to_num(input())
op = input()
b = to_num(input())

print("{:.2f}".format(opts[op](a, b)))
