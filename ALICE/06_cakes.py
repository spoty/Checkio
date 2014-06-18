import operator
o = {'+': operator.add, '-': operator.sub}


def checkio(k):
    m = lambda n: set([i for i in [c[n] for c in k] if [c[n] for c in k].count(i)>2])
    # d = [[x[0]-i, x[1]+i] for i in range(1,10)]
    d = lambda op1,op2:[[[o[op1](x[0],i), o[op2](x[1],i)]
            for i in range(1,10) if [o[op1](x[0],i), o[op2](x[1],i)] in k]
            for x in k]




    d1 = [x for x in d('-','+')+d('+','-') if len(x)>1]
    d2 = [x for x in d('-','-')+d('+','+') if len(x)>1]
    print d1
    print d2
    # print [[x[0]-i, x[1]+i] for i in range(1,10)] + [[x[0]+i, x[1]-i] for i in range(1,10)]

    # [[x[0]-i, x[1]-i] for i in range(1,10)]
    # [[x[0]+i, x[1]+i] for i in range(1,10)]




    return len(m(0))+len(m(1))


print checkio([[3, 3], [5, 5], [8, 8], [2, 8], [8, 2]]) == 2

print checkio([[2, 2], [2, 5],
[2, 8], [5, 2], [7, 2], [8, 2], [9, 2], [4, 5], [4, 8], [7, 5], [5, 8], [9, 8]]) == 6
