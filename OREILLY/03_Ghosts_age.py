import math


def fibo(n):
# test N if is a Fibonacci number
    x = 5*(n**2) + 4
    y = 5*(n**2) - 4
    if x == int(math.sqrt(x)) ** 2:
        return n
    elif y == int(math.sqrt(y)) ** 2:
        return n
    elif n == 0:
        return 0
    return -1


def checkio(opacity):
    n = 10000-opacity
    result = [fibo(x) for x in range(1, 5001)]
    a = 0
    for y, x in enumerate(result):
        if a == n:
            break
        else:
            a += x
    return y

print checkio(9999)
