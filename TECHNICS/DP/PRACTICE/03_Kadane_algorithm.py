"""
Kadane's algorithm

Kadane's algorithm consists of a scan through the array values, computing at
each position the maximum (positive sum) subarray ending at that position. This
subarray is either empty (in which case its sum is zero) or consists of one more
element than the maximum subarray ending at the previous position.
"""

def max_subarray(A):
    max_ending_here = max_so_far = 0
    for x in A:
        max_ending_here = max(0, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

print max_subarray([5,6,-90,7,12,-5,-9,4,-1,10,1,2,-5])
"""
A variation of the problem that does not allow zero-length subarrays to be
returned in the case that the entire array consists of negative numbers can be
solved with the following code:
"""

def max_subarray(A):
    max_ending_here = max_so_far = A[0]
    for x in A[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far


