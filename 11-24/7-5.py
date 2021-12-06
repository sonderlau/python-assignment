import collections
import string
alphabets = dict.fromkeys(string.ascii_uppercase, 0)
words = collections.defaultdict(lambda: 0)


while True:
    in_ = input()
     
    if in_ == "0000":
        break
    sentence = list(in_.split(" "))
    for x in sentence:
        x = x.upper()
        words[x] += 1
        for i in x:
            #? 单词不一定由字母组成
            if i.isalpha():
                alphabets[i] += 1

words = sorted(words.items(), key=lambda x: (x[1], x[0]))

alphabets = sorted(alphabets.items(), key=lambda x: x[0])


print("{:10}{:>8}".format(words[-1][0], words[-1][1]))
print("{:10}{:>8}".format(words[0][0], words[0][1]))


for k in alphabets:
    print("{:10}{:>8}".format(k[0], k[1]))
