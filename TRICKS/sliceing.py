def checkio(l):
    g = []
    def grouper(l):
        if len(l) <= 4:
            return g.append(l)
        else:
            g.append(l[:4])
            return grouper(l[1:])
    grouper(l)
    return g


# print grouper([1,2,3,4,5,6,7,8])
print checkio([1,2,3,4,5,6,7,8])

# subList = [theList[n:n+N] for n in range(0, len(theList), N)]
group = lambda t, n: [t[i:n+i] for i,_ in enumerate(t) if len(t[i:n+i])>=n]
print group([1,2,3,4,5,6,7,8],4)


L = [  [1, 2, 3,],
       [4, 5, 6,],
       [7, 8, 9,], ]

h, w = len(L), len(L[0])

print([[L[h-1-q][p-q]
        for q in range(min(p, h-1), max(0, p-w+1)-1, -1)]
        for p in range(h+w-1)])

