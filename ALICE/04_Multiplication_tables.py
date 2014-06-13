def summ(fun, G):
    return sum(int('0b'+(("".join(str(x) for x in fun[n:n+G]))),2)
                                         for n in range(0, len(fun), G))


def checkio(n, m):

    N, M = [int(x) for x in bin(n)[2:]], [int(x) for x in bin(m)[2:]]

    G=len(M)

    and_ = summ([x and y for x in N for y in M], G)
    or_ = summ([x or y for x in N for y in M], G)
    xor_ = summ([(1 if bool(x) ^ bool(y) else 0) for x in N for y in M], G)

    return and_+or_+xor_



print checkio(4,6)

# print checkio(2,7), checkio(2,7) == 28
# print checkio(7,2), checkio(7,2) == 18

# from itertools import izip, product, tee

# # Logic functions: take and return iterators of truth values

# def AND(a, b):
#     for p, q in izip(a, b):
#         yield p and q

# def OR(a, b):
#     for p, q in izip(a, b):
#         yield p or q

# def NOT(a):
#     for p in a:
#         yield not p

# def EQUIV(a, b):
#     for p, q in izip(a, b):
#         yield p is q

# def IMPLIES(a, b):
#     for p, q in izip(a, b):
#         yield (not p) or q

# def create(num=2):
#     ''' Returns a list of all of the possible combinations of truth for the given number of variables.
#     ex. [(T, T), (T, F), (F, T), (F, F)] for two variables '''
#     return list(product([True, False], repeat=num))

# def unpack(data):
#     ''' Regroups the list returned by create() by variable, making it suitable for use in the logic functions.
#     ex. [(T, T, F, F), (T, F, T, F)] for two variables '''
#     return [[elem[i] for elem in lst] for i, lst in enumerate(tee(data, len(data[0])))]

# def print_result(data, result):
#     ''' Prints the combinations returned by create() and the results returned by the logic functions in a nice format. '''
#     n = len(data[0])
#     headers = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[:n]
#     print headers + "|RESULT"
#     print '-' * len(headers) + '+------'
#     for row, result_cell in izip(data, result):
#         print ''.join({True: 'T', False:'F'}[cell] for cell in row) + '|' + '  ' + {True: 'T', False:'F'}[result_cell]

# if __name__ == '__main__':
#     data = create(num=3)
#     A, B, C = unpack(data)
#     result = IMPLIES(A, OR(B, C))
#     print_result(data, result)
