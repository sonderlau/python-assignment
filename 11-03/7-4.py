alpha = input()

if alpha.isalpha():
    if alpha.isupper():
        print(ord(alpha))
    else:
        print(alpha.upper())
