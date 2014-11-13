# from bisect import bisect_left


# def binary_search(a, x, lo=0, hi=None):   # can't use a to specify default for hi
#     hi = hi or len(a)                     # hi defaults to len(a)
#     pos = bisect_left(a,x,lo,hi)          # find insertion position
#     return pos if pos != hi and a[pos] == x else -1 # don't walk off the end


# def checkio(required, operations):
#     l = []
#     for i, x in enumerate(operations):
#         for y in xrange(x[0],x[1]+1):
#             if binary_search(sorted(l),y) == -1:
#                 l.append(y)
#         if len(l) >= required: return i + 1
#     return -1

def checkio(num, data):
    numbers = sorted([n for start, end in data for n in (start, end + 1)])
    segments = [(n1, n2 - 1) for n1, n2 in zip(numbers[:-1], numbers[1:])]
    painted = set()
    for i, (start, end) in enumerate(data):
        painted |= {(s, e) for s, e in segments if start <= s and e <= end}
        if sum([e - s + 1 for s, e in painted]) >= num:
            return i + 1
    return -1

from bisect import bisect


def count_painted(ranges):
    """
    Precondition: ranges has even number of elements
    """
    return sum(r - l + 1 for l, r in zip(ranges[::2], ranges[1::2]))


def checkio(required, operations):
    painted_ranges = [] # it contains ranges as a flat list
    for step, op in enumerate(operations):
        left, right = op
        left_index = bisect(painted_ranges, left)
        right_index = bisect(painted_ranges, right)
        if left_index % 2:
            if not right_index % 2:
                painted_ranges.insert(right_index, right)
        else:
            painted_ranges.insert(left_index, left)
            left_index += 1
            if not right_index % 2:
                painted_ranges.insert(right_index + 1, right)
            right_index += 1
        painted_ranges = painted_ranges[:left_index] + painted_ranges[right_index:]
        print painted_ranges
        if count_painted(painted_ranges) >= required:
            return step + 1
    return -1


# from itertools import accumulate

# def painted(ranges):
#     last = counter = total = 0
#     for pos, d in sorted(sum((((i-1, +1), (j, -1)) for (i, j) in ranges), ())):
#         if counter:
#             total += pos - last
#         counter += d
#         last = pos
#     return total

# def checkio(num, ranges):
#     for i, prefix in enumerate(accumulate([i] for i in ranges), start=1):
#         if painted(prefix) >= num:
#             return i
#     return -1
#print checkio(5, [[1,5], [11,15], [2,14], [21,25]]) == 1 # The first operation will paint 5 meter long.
#print checkio(6, [[1,5], [11,15], [2,14], [21,25]])# == 2 # The second operation will paint 5 meter long. The sum is 10.
# checkio(11, [[1,5], [11,15], [2,14], [21,25]]) == 3 # After the third operation, the range 1-15 will be painted.
print checkio(16, [[1,5], [11,15], [2,14], [21,25]]) == 4 # Note the overlapped range must be counted only once.
#checkio(21, [[1,5], [11,15], [2,14], [21,25]]) == -1 # There are no ways to paint for 21 meters from this list.
#print checkio(111, [[1, 100], [11, 110]])  == -1 # One of the huge test cases.

