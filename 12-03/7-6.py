lst = input().split(" ")
len_sum = 0
for i in lst:
    len_sum += len(i)
print(f"{len(lst)},{len_sum/len(lst):.2f}")
