Overlapping Subproblems # http://20bits.com/article/introduction-to-dynamic-programming

A problem is said to have overlapping subproblems if it can be broken down into
subproblems which are reused multiple times. This is closely related to
recursion. To see the difference consider the factorial function, defined as
follows(in Python):


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

Thus the problem of calculating factorial(n) depends on calculating the
subproblem factorial(n - 1). This problem does not exhibit overlapping subproblems
since factorial is called exactly once for each positive integer less than n.


Fibonacci Numbers
The problem of calculating the nth Fibonacci number does, however, exhibit
overlapping subproblems. The naive recursive implementation would be


def fib(n):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)


The problem of calculating fib(n) thus depends on both fib(n - 1) and fib(n - 2). To
see how these subproblems overlap look at how many times fib is called and with
what arguments when we try to calculate fib(5):


fib(5)
fib(4) + fib(3)
fib(3) + fib(2) + fib(2) + fib(1)
fib(2) + fib(1) + fib(2) + fib(2) + fib(1)


At the kth stage we only need to know the values of fib(k - 1) and fib(k - 2), but
we wind up calling each multiple times. Starting from the bottom and going up we
can calculate the numbers we need for the next step, removing the massive
redundancy.


def fib2(n):
    n1, n2 = 0, 1
    for i in range(n - 2):
        n1, n2 = n2, n2 + n1
    return n1 + n2


In Big - O notation the fib function takes O(cn) time, i.e., exponential in n,
while the fib2 function takes O(n) time.

The above problem is pretty easy and for most programmers is one of the first
examples of the performance issues surrounding recursion versus iteration. In
fact, I've seen many instances where the Fibonacci example leads people to
believe that recursion is inherently slow. This is not true, but in cases where
we can define a problem with overlapping subproblems recursively using the above
technique will always reduce the execution time.
