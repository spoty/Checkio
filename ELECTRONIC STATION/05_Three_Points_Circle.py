import math
def checkio(c):
    A, B, C = eval(c)
    a, b = 2*(B[0] - A[0]), 2*(B[1] - A[1])
    d, e = 2*(C[0] - B[0]), 2*(C[1] - B[1])
    ab = B[0]**2 + B[1]**2 - A[0]**2 - A[1]**2
    de = C[0]**2 + C[1]**2 - B[0]**2 - B[1]**2
    x, y = (b*de - e*ab)/float((b*d - e*a)), (d*ab - a*de)/float((b*d - e*a))
    r = math.sqrt((x - A[0])*(x - A[0])+(y - A[1])*(y - A[1]))
    def m(n):
        n = round(n,2)
        return int(n) if n == int(n) else n
    return "(x-{})^2+(y-{})^2={}^2".format(m(x), m(y), m(r))



# print checkio("(2,2),(6,2),(2,6)")
print checkio("(7,3),(9,6),(3,6)")
