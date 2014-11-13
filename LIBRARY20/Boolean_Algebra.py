o = {"conjunction": lambda a,b: a and b,
     "disjunction": lambda a,b: a or b,
     "implication": lambda a,b: not(a) or b,
     "exclusive": lambda a,b: a^b,
     "equivalence": lambda a,b: a==b}


def boolean(a,b,op):
    return o[op](a,b)

# boolean(0,0,"conjunction")

# import re

# def checkio(data):

#     #replace this for solution
#     if len(data)>=10 and re.match('[A-Za-z0-9]+[A-Z]+[0-9]+[a-z]', data):
#         return True
#     else:
#         return False

# print checkio('A1213pokl')
# print checkio('bAse730onE4')


