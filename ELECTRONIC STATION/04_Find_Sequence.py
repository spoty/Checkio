def checkio(l):
    g = lambda t, n: [t[i:n+i]
                        for i,_ in enumerate(t)
                        if len(t[i:n+i])>=n
                        and t[i:n+i].count(t[i:n+i][0])>=4]
# and t[i:n+i].count(t[i:n+i][0])>=4
# and t[i:n+i].count(t[i:n+i][0])==len(t[i:n+i])
    m = lambda f: [g(x,4) for x in f if g(x,4) != [] and len(x)>=4]

    h,w = len(l),len(l[0])

    nw_se =  [[l[h-1-q][p-q]
                        for q in range(min(p, h-1), max(0, p-w+1)-1, -1)]
                        for p in range(h+w-1)]

    ne_sw =  [[l[p-q][q]
                        for q in range(min(p, h-1), max(0, p-w+1)-1, -1)]
                        for p in range(h+w-1)]

    # print m(l)+m(map(None, *l))
    # print "-"*50
    # print m([x for x in nw_se+ne_sw if len(x)>=4 and x != []])
    # and and x.count(x[0])>=4

    return True if m(l+map(None, *l)+nw_se+ne_sw) else False








print checkio([
    [1, 2, 1, 1],
    [1, 1, 4, 1],
    [1, 3, 1, 6],
    [1, 7, 2, 5]
])
print checkio([
    [7, 1, 4, 1],
    [1, 2, 5, 2],
    [3, 4, 1, 3],
    [1, 1, 8, 1]
])
print checkio([
    [2, 1, 1, 6, 1],
    [1, 3, 2, 1, 1],
    [4, 1, 1, 3, 1],
    [5, 5, 5, 5, 5],
    [1, 1, 3, 1, 1]
])
print checkio([
    [7, 1, 1, 8, 1, 1],
    [1, 1, 7, 3, 1, 5],
    [2, 3, 1, 2, 5, 1],
    [1, 1, 1, 5, 1, 4],
    [4, 6, 5, 1, 3, 1],
    [1, 1, 9, 1, 2, 1]
    ])
