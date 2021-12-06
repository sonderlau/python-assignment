n = int(input())
dict1 = {}
list1 = []
for ppp in range(n):
    str = input()
    a = ''
    for i in str:
        if i.isalpha():
            a += i.lower()
        elif a != '':
            if a in list1:
                dict1[a] = dict1[a] + 1
                a = ''
            else:
                dict1[a] = 1
                list1.append(a)
                a = ''
    if a != '':
        if a in list1:
            dict1[a] = dict1[a] + 1
            a = ''
        else:
            dict1[a] = 1
            list1.append(a)
            a = ''
list1.sort()
for i in list1:
    print(i, dict1[i])