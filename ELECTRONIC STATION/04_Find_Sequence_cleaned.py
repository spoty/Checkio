def checkio(l):
    g = lambda t, n: [t[i:n+i]
                        for i,_ in enumerate(t)
                        if len(t[i:n+i])>=n
                        and t[i:n+i].count(t[i:n+i][0])>=4]
    m = lambda f: [g(x,4) for x in f if g(x,4) != [] and len(x)>=4]
    h,w = len(l),len(l[0])
    f = lambda i_1, i_2: [[l[eval(i_1)][eval(i_2)]
                    for q in range(min(p, h-1), max(0, p-w+1)-1, -1)]
                    for p in range(h+w-1)]
    d = f('h-1-q', 'p-q')+f('p-q', 'q')
    return True if m(l+map(None, *l)+d) else False

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
