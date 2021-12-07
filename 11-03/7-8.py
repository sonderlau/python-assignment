sum = 0
cnt = 0
while True:

    num = int(input())

    if num > 0:
        sum += num
        cnt += 1
    elif num == -1:
        print(" 输入了           {} 个正整数".format(cnt))
        print("平均值为：   {:.7f}  ".format(sum / cnt))
        break
