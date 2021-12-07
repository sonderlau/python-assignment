ele = input()
ele = int(ele)
unit = 0.538
if ele <= 230:
    sum = ele * unit
elif ele > 230 and ele <= 400:
    sum = 230 * unit + (ele - 230) * (unit + 0.05)
else:
    sum = 230 * unit + 170 * (unit + 0.05) + (ele - 400) * (unit + 0.05 + 0.3)

print("{:.2f}".format(sum))
