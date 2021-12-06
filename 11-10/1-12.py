s = input()

x = reversed(s)

print(s, end="")
if list(s) == list(x):
    print("是回文。")
else:
    print("不是回文。")