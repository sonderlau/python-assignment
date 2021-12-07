while True:
    down, top = map(int, input().split(" "))
    if top <= down:
        print("Done")
        break
    sum = 0
    for i in range(down, top + 1):
        sum += i ** 2

    print("The sum of the squares from {} to {} is {}".format(down ** 2, top ** 2, sum))
