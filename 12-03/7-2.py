from icecream import ic

while True:
    try:
        r = input()
        if len(r) % 2 != 0:
            print(len(r))
            continue
        else:
            size = len(r)
            half = int(size / 2)
            front = r[:half]
            ladder =r [half:][::-1]
            ic(front, ladder)
            while (front == ladder):
                size = int(size / 2)
                half = int(size / 2)
                
                front = r[:half]
                ladder =r [half:size][::-1]
                
                ic(front, ladder, size, half)
                
            
            print(size)
            
    except EOFError:
        break