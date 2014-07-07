def checkio(number):
    x, n = 0, 1
    while number > 0:
        x, n = x + n, n + 1
        number -= x
        if (number + x) < x:
            if (number + x) < (x - n):
                return x - (n - 1)
            else:
                return number + x
        if number == 0:
            return x

checkio(50)


# Recursive
def pigeons(w, c=0, i=1):
    if w <= c:
        return max(c - i + 1, w)
    else:
        w, c, i = w - c, c + i, i + 1
        return pigeons(w, c, i)

print pigeons(5)
print pigeons(10)
print pigeons(11)
# def checkio(number):
#     x, n = 0, 1

#     while number > 0:
#         x, n =  x + n, n + 1
#         number = number - x
# print "before SUPPLY: %s, BIRDS: %s, after SUPPLY: %s" % (number + x, x, number)
# print "N %s" % n
#         if (number + x) < x:
#             if (number + x) < (x - n):
# print x - (n-1)
#                 return x - (n-1)
#             else:
# print number + x
#                 return number + x
#         if number == 0:
# print x
#             return x

# Recursive


# def pigeons(w, c=0, i=1):
#     if w <= c:
#         return c - i + 1 if w < c - i + 1 else (c - i + 1) + w - (c - i + 1)
#     else:
#         w, c, i = w - c, c + i, i + 1
#         return pigeons(w, c, i)
