from __future__ import division

import re
from decimal import Decimal, getcontext

def convert(n,d):
    getcontext().prec = 2000
    if len(str(n/Decimal(d))) >=2000:
        RD = re.match(r'(.+?)(.+?)\2{2,}\1*', str(n/Decimal(d)))
        return "{}({})".format(RD.group(1), RD.group(2))
    if n%d == 0 or n == 0: return str(int(n/d))+'.'
    return str(n/d)


# def gcd(a, b):
#     """Computes gcd of a, b
#     using Euclid algorithm.

#     """
#     if not isinstance(a, int) or not isinstance(b, int):
#         return None
#     a = abs(a)
#     b = abs(b)
#     while b != 0:
#         a, b = b, a % b
#     return a

# def decimal(p, q):
#     """Computes the decimal representation
#     of the rational number p/q. If the
#     representation is non-terminating, then
#     the recurring part is enclosed in parentheses.
#     The result is returned as a string.

#     """
#     if not isinstance(p, int) or not isinstance(q, int):
#         return ''
#     if q == 0:
#         return ''
#     abs_p = abs(p)
#     abs_q = abs(q)
#     s = (p / abs_p) * (q / abs_q)
#     g = gcd(abs_p, abs_q)
#     p = abs_p / g
#     q = abs_q / g
#     rlist = []
#     qlist = []
#     quotient, remainder = divmod(p, q)
#     qlist.append(quotient)
#     rlist.append(remainder)
#     if remainder == 0:
#         return str(quotient)
#     while remainder != 0:
#         remainder *= 10
#         quotient, remainder = divmod(remainder, q)
#         qlist.append(quotient)

#         if remainder in rlist:
#             break
#         else:
#             rlist.append(remainder)
#     qlist = map(str, qlist)
#     if remainder:
#         recur_index = rlist.index(remainder) + 1
#         dstring = qlist[0] + '.' + ''.join(qlist[1:recur_index]) + \
#             '(' + ''.join(qlist[recur_index:]) + ')'
#         if s < 0:
#             dstring = '-' + dstring
#     else:
#         dstring = qlist[0] + '.' + ''.join(qlist[1:])
#         if s < 0:
#             dstring = '-' + dstring
#     return dstring


# print decimal(1, 999)

print convert(1,3)
# print convert(7, 11)
# print convert(3,8)
# print convert(0,2)
# print convert(4,2)
# print convert(27,26)
# print convert(23,2)
# print convert(58,23)
# print convert(1,999)
# print convert(20,6)

