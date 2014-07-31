Table of common time complexities
=================================

Name                         Running time (T(n))        Example algorithms
--------------------------------------------------------------------------
constant time                O(1)                       Determining if an integer (represented in binary) is even or odd
inverse Ackermann time       O(α(n))                    Amortized time per operation using a disjoint set
iterated logarithmic time    O(log* n)                  Distributed coloring of cycles
log-logarithmic              O(log log n)               Amortized time per operation using a bounded priority queue[2]
logarithmic time             O(log n)                   Binary search
polylogarithmic time         poly(log n)
fractional power             O(n**c) where 0 < c < 1    Searching in a kd-tree
linear time                  O(n)                       Finding the smallest item in an unsorted array
"n log star n" time          O(n log* n)                Seidel's polygon triangulation algorithm.
linearithmic time            O(n log n)                 Fastest possible comparison sort
quadratic time               O(n**2)                    Bubble sort; Insertion sort; Direct convolution
cubic time                   O(n**3)                    Naive multiplication of two n×n matrices. Calculating partial correlation.
polynomial time              2**O(log n) = poly(n)      Karmarkar's algorithm for linear programming; AKS primality test
quasi-polynomial time        2**poly(log n)             Best-known O(log2 n)-approximation algorithm for the directed Steiner tree problem.
sub-exponential time         O(2**n**ε) for all ε > 0   Assuming complexity theoretic conjectures, BPP is contained in SUBEXP.[3]
(first definition)
sub-exponential time         2**o(n)                    Best-known algorithm for integer factorization and graph isomorphism
(second definition)
exponential time             2**O(n)                    Solving the traveling salesman problem using dynamic programming
(with linear exponent)
factorial time               O(n!)                      Solving the traveling salesman problem via brute-force search
exponential time             2**poly(n)                 Solving matrix chain multiplication via brute-force search
double exponential time      2**2**poly(n)              Deciding the truth of a given statement in Presburger arithmetic



O(1):
the constant time algorithm which always takes a fixed number of steps
for any input. For example, looking up a key in a hash table.

O(\log n):
logarithmic time, where at each step of the algorithm the problem size is
reduced by a fixed factor. This is common to “divide and conquer” algorithms.

O(n^c) for c > 0:
polynomial time. If f(n) is not a monomial, we conventionally
drop all terms but the one of highest degree, because under the limit the
highest degree term dominates the runtime.

O(a^n) for a > 1:
exponential time,
where with each increase of the input size, the runtime increases by a factor
of a. This is extremely slow for any reasonable input size, even when a is very
close to 1. Many brute-force algorithms (attempting every possibility) result
in exponential runtime.

O(n!):
factorial time, which is often clumped with
exponential time, is actually strictly slower than any exponential time
algorithm. Considering s_n = a^n / n!, as n surpasses a, we have each s_n =
s_{n-1} (\frac{a}{n}), and since a < n, we decrease s_n at each step, and the
limit goes to 0 (i.e., factorials grow much faster). Travelling Salesman is a
famous problem whose brute-force solution is factorial, but even with cutting-
edge methods for optimization, the worst case runtime is still exponential.

