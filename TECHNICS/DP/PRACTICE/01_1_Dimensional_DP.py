""""
Problem:
given n , find the number of different ways to write n as the sum of 1, 3, 4
Example: for n = 5 , the answer is 6
"""
# 1. Define subproblems
"""  Dn is number of ways how to sum 1,3,4 to get n  """
# 2. Write down the recurrence that relates subproblems
"""
    1. n = x1 + x2 + ... + xm
    2. if xm = 1 then rest sum to n-1
    3. Thus, number of sums that end with xm = 1 is equal to Dn-1
    4. Dn = Dn-1 + Dn-3 + Dn-4
"""
# 3. Recognize and solve the base cases

def checkio(n):
    D=[1,1,1,2]
    for i in range(4, n+1):
        D.append(D[i-1] + D[i-3] + D[i-4])
    print D

checkio(5)

def checkio(n):
    from itertools import product
    m = []
    for x in range(1,n+1):
        m.extend(list(product([1,3,4],repeat=x)))
    return len([x for x in m if sum(x) == n])

print checkio(5)
