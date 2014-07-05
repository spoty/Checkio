"""
Input: Two arguments. A pattern as a list of lists and an image as a list of lists.

Output: The marked image as a matrix as a list of list.

Precondition:

1 < image_width <= 10
1 < image_height <= 10
1 < pattern_height <= 10
1 < pattern_height <= 10
|pattern| < |image|
V x from data : x == 0 or x == 1
"""


def find(haystack, needle):
    """Return the index at which the sequence needle appears in the
    sequence haystack, or -1 if it is not found, using the Boyer-
    Moore-Horspool algorithm. The elements of needle and haystack must
    be hashable.

    >>> find([1, 1, 2], [1, 2])
    1

    """
    h = len(haystack)
    n = len(needle)
    skip = {needle[i]: n - i - 1 for i in range(n - 1)}
    i = n - 1
    while i < h:
        for j in range(n):
            if haystack[i - j] != needle[-j - 1]:
                i += skip.get(haystack[i], n)
                break
        else:
            return (i - n + 1), (i - n + 1) + 2
    return 0


def checkio(pattern, image):
    N = len(pattern[0])



    for i, row in enumerate(image):

        for p in range(5):
            print p
            if find(row, pattern[0]) != 0:
                a, b = find(row, pattern[0])

                if [f[a:b] for f in image[i:i + N] if a + b > 0] == pattern:
                    for row in image[i:i + N]:
                        row[a:b] = map(lambda x: 2 if x == 0 else 3, row[a:b])




            # for f in image[i:i+N]:
            #     print f[a:b]

    for x in image:
        print x
    return []

checkio([[1, 0], [1, 1]],
        [[0, 1, 0, 1, 0],
         [0, 1, 1, 0, 0],
         [1, 0, 1, 1, 0],
         [1, 1, 0, 1, 1],
         [0, 1, 1, 0, 0]]) == [[0, 3, 2, 1, 0],
                               [0, 3, 3, 0, 0],
                               [3, 2, 1, 3, 2],
                               [3, 3, 0, 3, 3],
                               [0, 1, 1, 0, 0]]
# checkio([[1, 1], [1, 1]],
#         [[1, 1, 1],
#          [1, 1, 1],
#          [1, 1, 1]]) == [[3, 3, 1],
#                          [3, 3, 1],
#                          [1, 1, 1]]
