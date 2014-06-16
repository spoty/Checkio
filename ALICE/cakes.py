import operator
o = {'+': operator.add, '-': operator.sub}


def checkio(cakes):
    m = lambda n: set([i for i in [c[n] for c in cakes] if [c[n] for c in cakes].count(i)>2])
    # d = [[x[0]-i, x[1]+i] for i in range(1,10)]
    d = lambda op1,op2: [[[o[op1](x[0],i), o[op2](x[0],i)] for i in range(1,10) if [o[op1](x[0],i), o[op2](x[0],i)] in cakes] for x in cakes]

    print d('-','+')+d('+','-')
    print d('-','-')+d('+','+')

    # print [[x[0]-i, x[1]+i] for i in range(1,10)] + [[x[0]+i, x[1]-i] for i in range(1,10)]

    # [[x[0]-i, x[1]-i] for i in range(1,10)]
    # [[x[0]+i, x[1]+i] for i in range(1,10)]



    print len(m(0))+len(m(1))
    return len(m(0))+len(m(1))


print checkio([[3, 3], [5, 5], [8, 8], [2, 8], [8, 2]]) == 2

# print checkio([[2, 2], [2, 5],
# [2, 8], [5, 2], [7, 2], [8, 2], [9, 2], [4, 5], [4, 8], [7, 5], [5, 8], [9, 8]]) == 6
