n = input()

sum = 0

for i in range(0, len(n)):
    sum += int(n[i])
    
print("{} {}".format(len(n), sum))