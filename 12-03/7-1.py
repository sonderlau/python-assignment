from collections import defaultdict

m = int(input())

for y in range(0, m):
    n = int(input())
    d = defaultdict(lambda : 0)
    for x in range(0, int(n*(n - 1) / 2)):
        winner, loser, f = input().split(" ")
    
        if f == "0":
            d[winner] += 1
            d[loser] += 1
        else:
            d[winner] += 3
            d[loser] += 0
        
        r = sorted(d.items(), key= lambda x: (-x[1], x[0]))
    
    
    cnt = 1
    tmp = -1
    for one in r:
        if one[1] != tmp:
            if cnt != 1:
                print()
            print(cnt, end="")
        
        print(" " + one[0], end="")
        cnt += 1
        tmp = one[1]
    print()
        
    
    
    