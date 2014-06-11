# from __future__ import division
import math

# print 4.0 % 1

def triangular(n):
    return n*(n+1)/2


def checkio(n):
    x = [i*(i+1)/2 for i in range(n)]
    a = n**(1/3.0)
    print int(a)
    # y = triangular(a)
    # rez = x[y-a:y]
    # return rez


print checkio(64)

# print triangular(4)

# n = 64
# print math.pow(n,1/3)
