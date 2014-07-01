import string


def checkio(u):
    # d = {k:v for k,v in zip(string.ascii_uppercase, range(10,36))}
    # l = []
    # for x in u:
    #     if x in string.ascii_uppercase:
    #         l.append(d[x])
    #     else: l.append(x)

    # l = [int(x) for x in l]
    l = [int(x, 36) for x in u]
    m = max(l)
    def radix(l, i=0, r=0):
        if len(l) == 0: return r
        else:
            r += l[-1]*(m+1)**i
            i += 1
            return radix(l[:-1], i, r)
    while radix(l)%(m) !=0:
        m += 1
        radix(l)
        if m > 36: return 0
    return m+1

print checkio(u"18") == 10
print checkio(u"1010101011") == 2
print checkio(u"222") == 3
print checkio(u"A23B") == 14
print checkio(u"IDDQD") == 0


# def checkio(number):
#     max_digit = int(max(number), 36)
#     for k in range(max_digit+1, 37):
#         if int(number, k) % (k-1) == 0:
#             return k
#     return 0

# def checkio(number):
#     for k in range(2, 37):
#         try:
#             if int(number, k) % (k - 1) == 0:
#                 return k
#         except ValueError:
#             continue
#     return 0

# def checkio(number):

#     start = int(max(number), 36) + 1
#     rs = [r for r in range(start, 37) if int(number, r) % (r-1) == 0]

#     return min(rs) if rs else 0
