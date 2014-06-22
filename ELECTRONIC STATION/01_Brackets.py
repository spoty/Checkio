BRACKETS = ["()", "[]", "{}"]

def checkio(u):
    u = "".join(x for x in u if x in "()[]{}")
    for i in range(len(u)):
        for x in BRACKETS:
            u=u.replace(x, '')
    return True if not u else False

# def checkio(astr):
#     stack = []
#     for c in astr:
#         d = parens.get(c, None)
#         if d:
#             stack.append(d)
#         elif c in closing:
#             if not stack or c != stack.pop():
#                 return False
#     return not stack

print checkio("((([{}])))")
print checkio("[[]]0410")
print checkio(u"((5+3)*2+1)")
print checkio(u"{[(3+1)+2]+}")
print checkio(u"(3+{1-1)}")
print checkio("[1+1]+(2*2)-{3/3}")
