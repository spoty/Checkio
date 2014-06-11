# def T_T(b,a):
#     return ((a*(a+1)*(a+2))/6)-(b*(b+1)*(b+2)/6)+(b*(b+1)/2)

# def f(n):
#     return n*(n+1)*(n+2)/6

# def triangular(n):
#     return n*(n+1)/2

# def checkio(n):
#     def has_integer_cube_root(n):
#         floatroot = (n ** (1.0 / 3.0))
#         introot = int(round(floatroot))
#         return (introot*introot*introot == n, introot)

#     x = [i*(i+1)/2 for i in range(n)]

#     if has_integer_cube_root(n)[0]: a = has_integer_cube_root(n)[1]
#     else: return []
#     y = triangular(a)
#     rez = x[y-a:y+1]
#     return rez, sum(rez)


def checkio(n):
    for start in range(1, n + 1):
        for end in range(start, n + 1):
            t_seq = [i*(i+1)/2 for i in range(start, end + 1)]
            rez = sum(t_seq)
            if rez == n: return t_seq
            elif rez > n: break
    return []

print checkio(64)
