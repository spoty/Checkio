""" Partition problem: http://en.wikipedia.org/wiki/Partition_problem
http://www.americanscientist.org/issues/pub/2002/3/the-easiest-hard-problem/
http://web.cecs.pdx.edu/~bart/cs510ai/papers/korf-ckk.pdf

Input data:
A list of the weights as a list of integers.

Output data:
The number representing the lowest possible weight difference as a positive
integer.
"""


import random import math

def greedy(numbers):
    """
    The greedy algorithm
    """
    a = []
    b = []
    numo = sorted(numbers, reverse=True)
    for x in numo:
        if sum(a) <= sum(b):
            a.append(x)
        else:
            b.append(x)
    return abs(sum(a)-sum(b))


def Karmarkar_karp(numbers):
    """
    Karmarkar-Karp algorithm
    """
    numo = sorted(numbers, reverse=True)
    while len(numo) > 1:
        if numo[1] == 0: return [numo[0]]
        diff = abs(numo[0]-numo[1])
        if numo[1]:
            if numo[1]: numo.remove(numo[1])
            if numo[0]: numo.remove(numo[0])
            numo.append(diff)
            numo = sorted(numo, reverse=True)
    return numo


def checkio(weights):
    """
    Inspired by: Balanced Partition
    http://people.csail.mit.edu/bdean/6.046/dp/dp_4.swf
    """
    best = sum(weights)
    bests = ()
    target = best/2

    P = {}
    P[-1] = {0:()}

    for i in range(len(weights)):
        x = weights[i]
        P[i] = {}
        for j in P[i-1].keys():
            P[i][j] = P[i-1][j]
            if j+x > target:
                continue
            P[i][j+x] = P[i-1][j] + (x,)
            if abs((j+x)-target)<abs(best-target):
                best = j+x
                bests = P[i][j+x]
                if best == target:
                    break

    def sub(weights, bests):
        bests = list(bests)
        return sum([x for x in weights if not x in bests or bests.remove(x)])

    return abs(sum(bests)-sub(weights, bests))


# print Karmarkar_karp([9,9,7,6,5])
# print Karmarkar_karp([12, 30, 30, 32, 42, 49])
# print Karmarkar_karp([10,10])
# print Karmarkar_karp([10])
# print Karmarkar_karp([3, 3])
# print Karmarkar_karp([5,5,6,5])
# print Karmarkar_karp([12, 30, 30, 32, 42, 49])
# print Karmarkar_karp([1, 1, 1, 3])
# print Karmarkar_karp([12, 30, 30, 32, 42, 49])
# print Karmarkar_karp([771, 121, 281, 854, 885, 734, 486, 1003, 83, 62])

print checkio([5,10,5,10,1])
print checkio([9,9,7,6,5])
print checkio([12, 30, 30, 32, 42, 49])
print checkio([10,10])
print checkio([10])
print checkio([3, 3])
print checkio([5,5,6,5])
print checkio([12, 30, 30, 32, 42, 49])
print checkio([1, 1, 1, 3])
print checkio([12, 30, 30, 32, 42, 49])
print checkio([771, 121, 281, 854, 885, 734, 486, 1003, 83, 62])
