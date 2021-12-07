from math import sqrt

a, b, c = map(float, input().split(" "))

delta = b * b - 4 * a * c

if delta < 0:
    print("-1 -1")
else:
    solutions = []

    solution_1 = (-b + sqrt(delta)) / (2 * a)
    solution_2 = (-b - sqrt(delta)) / (2 * a)
    solutions.append(solution_1)
    solutions.append(solution_2)
    solutions.sort()
    print("{:.2f} {:.2f}".format(solutions[0], solutions[1]))
