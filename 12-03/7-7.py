v = list(eval(input()))
print("before:", v)
v.reverse()
vv = [""]
for i in v:
    if i not in vv:
        vv.insert(0, i)
vv.pop()
print("after:", vv, end="")
