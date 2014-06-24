import math
def checkio(c):
    A, B, C = eval(c)

    a, b = 2*(B[0] - A[0]), 2*(B[1] - A[1])
    d, e = 2*(C[0] - B[0]), 2*(C[1] - B[1])

    c = B[0]**2 + B[1]**2 - A[0]**2 - A[1]**2
    f = C[0]**2 + C[1]**2 - B[0]**2 - B[1]**2

    x = (b*f - e*c)/float((b*d - e*a))
    y = (d*c - a*f)/float((b*d - e*a))
    r = math.sqrt((x - A[0])*(x - A[0])+(y - A[1])*(y - A[1]))

    x, y, r = round(x,2), round(y,2), round(r,2)
    if x == int(x): x = int(x)
    if y == int(y): y = int(y)
    if r == int(r): r = int(r)

    return "(x-{0})^2+(y-{1})^2={2}^2".format(str(x), str(y), str(r))



print checkio("(2,2),(6,2),(2,6)")
