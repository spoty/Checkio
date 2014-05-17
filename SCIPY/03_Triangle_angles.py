from math import acos, degrees

def checkio(*d):
    """
    Return the interior angles of a triangle.
    """
    d = sorted(d)
    if d[0]+d[1]>d[2]:
        a = [(d[0] * d[0] + d[1] * d[1] - d[2] * d[2])/(2.0 * d[0] * d[1]),
            (d[0] * d[0] + d[2] * d[2] - d[1] * d[1])/(2.0 * d[0] * d[2]) ]
        rez = [int(round(degrees(acos(x)))) for x in a]
        return [rez[0],rez[1], (180-(rez[0]+rez[1]))]
    return [0,0,0]


# from math import*
# checkio=lambda*s:sorted(round(180/pi*acos((sum(x*x for x in
# s)-2*x*x)*x/2/exp(sum(map(log,s)))))if 0<min(s)<2*max(s)<sum(s)else 0for x in s)

# def checkio(a, b, c):
#     a, b, c = sorted((a, b, c))
#     if a + b <= c:
#         return [0, 0, 0]
#     a2, b2, c2 = a**2, b**2, c**2
#     angles = (math.acos((a2+b2-c2) / (2*a*b)),
#               math.acos((a2+c2-b2) / (2*a*c)),
#               math.acos((b2+c2-a2) / (2*b*c)))
#     return list(sorted(round(math.degrees(a)) for a in angles))

print checkio(4, 4, 4)
print checkio(3, 4, 5)
print checkio(2, 2, 5)
