def checkio(n):
    a, d  = '', 9
    while d > 1:
        if n%d != 0:
            d -= 1
        else:
            a = str(d) + a
            n /= d
    return int(a) if n == 1 else 0

# def checkio(n):
#     if n <= 1: return n
#     l = ""
#     for r in "98765432":
#         while n > 1:
#             d, m = divmod(n, int(r))
#             if m != 0: break
#             n = d
#             l = r + l
#     return int(l) if n == 1 else 0


print checkio(25)
