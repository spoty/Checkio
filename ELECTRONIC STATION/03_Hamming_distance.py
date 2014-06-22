def checkio(a,b):
    f = len(str(bin(max(a,b)))[2:])
    z = zip(str(bin(a))[2:].zfill(f),str(bin(b))[2:].zfill(f))
    return sum(1 for i,_ in enumerate(z) if z[i][0] != z[i][1])

# def checkio(a,b):
#     f = len(str(bin(max(a,b)))[2:])
#     z = map(lambda x: x[0]==x[1] ,zip(str(bin(a))[2:].zfill(f),str(bin(b))[2:].zfill(f)))
#     return len(z)-sum(z)

# def checkio(a,b):
#     f = len(str(bin(max(a,b)))[2:])
#     o = lambda c: [int(x) for x in str(bin(c))[2:].zfill(f)]
#     z = map(lambda x: x[0]==x[1] ,map(None, *[o(a), o(b)]))
#     return len(z)-sum(z)

print checkio(117, 17)
print checkio(1, 2)
print checkio(16, 15)
