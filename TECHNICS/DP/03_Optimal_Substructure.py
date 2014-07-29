Optimal Substructure # http://en.wikipedia.org/wiki/Optimal_substructure
--------------------
A problem is said to have optimal substructure if the globally optimal solution
can be constructed from locally optimal solutions to subproblems. The general
form of problems in which optimal substructure plays a roll goes something like
this. Let's say we have a collection of objects called A. For each object o in A
we have a "cost," c(o). Now find the subset of A with the maximum (or minimum)
cost, perhaps subject to certain constraints.

The brute-force method would be to generate every subset of A, calculate the
cost, and then find the maximum (or minimum) among those values. But if A has n
elements in it we are looking at a search space of size 2n if there are no
constraints on A. Oftentimes n is huge making a brute-force method
computationally infeasible. Let's take a look at an example.

Maximum Subarry Sum
-------------------
Let's say we're given an array of integers. What (contiguous) subarray has the
largest sum? For example, if our array is [1,2,-5,4,7,-2] then the subarray with
the largest sum is [4,7] with a sum of 11. One might think at first that this
problem reduces to finding the subarray with all positive entries, if one
exists, that maximizes the sum. But consider the array [1,5,-3,4,-2,1]. The
subarray with the largest sum is [1, 5, -3, 4] with a sum of 7.

First, the brute-force solution. Because of the constraints on the problem,
namely that the subsets under consideration are contiguous, we only have to
check O(n2) subarrays (why?). Here it is, in Python:

def msum(a):
    return max((sum(a[j:i]), (j,i)) for i in range(1,len(a)+1) for j in range(i))


This returns both the sum and the offsets of the subarray. Let's see if we can't
find an optimal substructure to exploit.

We are given an input array a. I'm going to use Python notation so that a[0:k]
is the subarray starting at 0 and including every element up to and including
k-1. Let's say we know the subarray of a[0:i] with the largest sum (and that
sum). Using just this information can we find the subarray of a[0:i+1] with the
largest sum?

Let a[j:k+1] be the optimal subarray, t the sum of a[j:i], and s the optimal
sum. If t+a[i] is greater than s then set a[j:i+1] as the optimal array and set
s = t. If t + a[i] is negative, however, the contiguity constraint means that we
cannot include a[j:i+1] in our subarray since any such subarray will have a
smaller sum than a subarray without it. So, if t+a[i] is negative set t = 0 and
set the left-hand bound of the optimal subarray to i+1.

To visualize consider the array [1,2,-5,4,7,-2].


Set s = -infinity, t = 0, j = 0, bounds = (0,0)
(1   2  -5   4   7  -2
(1)| 2  -5   4   7  -2  (set t=1.  Since t > s, set s=1 and bounds = (0,1))
(1   2)|-5   4   7  -2  (set t=3.  Since t > s, set s=3, and bounds = (0,2))
 1   2  -5(| 4   7  -2  (set t=-2. Since t < 0, set t=0 and j = 3 )
 1   2  -5  (4)| 7  -2  (set t=4.  Since t > s, set s=4 and bounds = (3,4))
 1   2  -5  (4   7)|-2  (set t=11. Since t > s, set s=11 and bounds = (3,5))
 1   2  -5  (4   7) -2| (set t=9.  Nothing happens since t < s)


This requires only one pass through the array and at each step we're only
keeping track of three variables:  the current sum from the left-hand edge of
the bounds to the current point (t), the maximal sum (s), and the bounds of the
current optimal subarray (bounds).


def msum2(a):
    bounds, s, t, j = (0,0), -float('infinity'), 0, 0

    for i in range(len(a)):
        t = t + a[i]
        if t > s: bounds, s = (j, i+1), t
        if t < 0: t, j = 0, i+1
    return (s, bounds)


In this problem the "globally optimal" solution corresponds to a subarray with a
globally maximal sum, but at each each step we only make a decision relative to
what we have already seen. That is, at each step we know the best solution thus
far, but might change our decision later based on our previous information and
the current information. This is the sense in the problem has optimal
substructure. Because we can make decisions locally we only need to traverse the
list once, reducing the run-time of the solution to O(n) from O(n2).
