""" Leonardo Pisano Fibonacci
1, 1, 2, 3, 5, 8, ...

F(n) = F(n - 1) + F(n - 2)
"""

# Recursive


def F_r(n):
    if n <= 2:
        return 1
    else:
        return F_r(n - 1) + F_r(n - 2)

# for x in range(1,21):
#     print F_r(x)
print F_r(5)

"""
But note that this is not quite efficient. Why? At each level of the recursion
you spawn two more recursions, which, by definition, are completely isolated
from each other. Okay, great, that's part of the solution! But notice that
"""
#    F(n - 1) = F(n - 2) + F(n - 3)
"""
In the first recursion that you spawn, you spawn another (sub)recursion that is
exactly the same as the second recursion you spawned initially! Of course your
computer doesn't know that, so it recomputes F(n - 2) twice, F(n - 3) three
times, and so on... leading to a very slow algorithm!

That's where dynamic programming comes in! You simply remember (cache) the
result for each of the possible values of n, and then reuse the result when you
need the same value again. One way to do this is to allocate an array where to
store the results:
"""

# def F_dp(n):
#     seq = [0, 1, 1]
#     for i in range(n-1):
#         seq[2] = seq[1] + seq[0]
#         seq[0] = seq[1]
#         seq[1] = seq[2]
#     return seq[2]

# print F_dp(6)

def F_dp(n):
    seq = [1, 1]
    for i in range(n-2):
        seq[0], seq[1] = seq[1], seq[1] + seq[0]
    return seq[1]

print F_dp(6)
