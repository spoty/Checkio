from itertools import permutations
import collections


def checkio(k):
    def get_line(a,b):
        if (b[1]-a[1]) == 0:
            m = 'h'
            i = a[1]
        else:
            try:
                m = (b[1]-a[1])/float((b[0]-a[0]))
                i = a[1]-m*a[0]
            except ZeroDivisionError:
                m = 'v'
                i = a[0]
        return m,i
    lines = collections.defaultdict(set)
    for points in permutations([tuple(x) for x in k], 2):
        line = get_line(points[0],points[1])
        for p in points:
            lines[line].add(p)

    return len([(x[0],x[1]) for x in lines.items() if len(x[1])>2])


# def checkio(k):
#     def get_line(a,b):
#         try:
#             m = (b[1] - a[1])/float((b[0]-a[0]))
#         except ZeroDivisionError:
#             m = 0
#         i = a[1] - m*a[0]
#         return m,i

#     k =[tuple(x) for x in k]
#     # horizontal + vertical
#     m = lambda n: set([i for i in [c[n] for c in k] if [c[n] for c in k].count(i)>2])
#     #diagonal lines
#     lines = collections.defaultdict(set)
#     for points in permutations(k, 2):
#         line = get_line(points[0],points[1])
#         if line[0] == 0: continue
#         for p in points:
#             lines[line].add(p)

#     return len([x[1] for x in lines.items() if len(x[1])>2])+len(m(0))+len(m(1))
