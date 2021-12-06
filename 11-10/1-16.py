words = input()



words.replace(",", " ")



words = words.split(" ")

first = words[0]
words.sort(key = lambda i:len(i))

if words[0] == words[-1]:
    print(first)
else:
    print(words[-1])
    print(words[0])
    