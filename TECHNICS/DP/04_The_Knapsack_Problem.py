The Knapsack Problem

Let's apply what we're learned so far to a slightly more interesting problem.
You are an art thief who has found a way to break into the impressionist wing at
the Art Institute of Chicago. Obviously you can't take everything. In
particular, you're constrained to take only what your knapsack can hold — let's
say it can only hold W pounds. You also know the market value for each painting.
Given that you can only carry W pounds what paintings should you steal in order
to maximize your profit?

First let's see how this problem exhibits both overlapping subproblems and
optimal substructure. Say there are n paintings with weights w1, ..., wn and
market values v1, ..., vn. Define A(i,j) as the maximum value that can be
attained from considering only the first i items weighting at most j pounds as
follows.

Obviously A(0,j) = 0 and A(i,0) = 0 for any i ≤ n and j ≤ W. If wi > j then
A(i,j) = A(i-1, j) since we cannot include the ith item. If, however, wi ≤ j
then A(i,j) then we have a choice: include the ith item or not. If we do not
include it then the value will be A(i-1, j). If we do include it, however, the
value will be vi + A(i-1, j - wi). Which choice should we make? Well, whichever
is larger, i.e., the maximum of the two.

Expressed formally we have the following recursive definition:
# http://20bits.com/article/introduction-to-dynamic-programming#knapsack

This problem exhibits both overlapping subproblems and optimal substructure and
is therefore a good candidate for dynamic programming. The subproblems overlap
because at any stage (i,j) we might need to calculate A(k,l) for several k < i
and l < j. We have optimal substructure since at any point we only need
information about the choices we have already made.

The recursive solution is not hard to write:

def A(w, v, i,j):
    if i == 0 or j == 0: return 0
    if w[i-1] > j:  return A(w, v, i-1, j)
    if w[i-1] <= j: return max(A(w,v, i-1, j), v[i-1] + A(w,v, i-1, j - w[i-1]))

Remember we need to calculate A(n,W). To do so we're going to need to create an
n-by-W table whose entry at (i,j) contains the value of A(i,j). The first time
we calculate the value of A(i,j) we store it in the table at the appropriate
location. This technique is called memoization and is one way to exploit
overlapping subproblems.

To exploit the optimal substructure we iterate over all i <= n and j <= W, at
each step applying the recursion formula to generate the A(i,j) entry by using
the memoized table rather than calling A() again. This gives an algorithm which
takes O(nW) time using O(nW) space and our desired result is stored in the
A(n,W) entry in the table.
