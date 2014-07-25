from collections import deque


# def rotate(c, p):
#     c, r = deque(c), []
#     for n in range(len(c)):
#         if all(c[i] for i in p):
#             r.append(n)
#         c.rotate(1)
#     return r

def rotate(fs, bb):
    return [i for i in range(len(fs)) if all(fs[b - i] for b in bb)]

print rotate([1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1], [0, 1]) == [1, 8]
print rotate([1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1], [0, 1, 2]) == []
print rotate([1, 0, 0, 0, 1, 1, 0, 1], [0, 4, 5]) == [0]
print rotate([1, 0, 0, 0, 1, 1, 0, 1], [5, 4, 5]) == [0, 5]





# shift = lambda l,s: l[-s:]+l[:-s]
