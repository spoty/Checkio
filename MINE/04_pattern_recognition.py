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

def find(pattern, row, L=len):
    return [(index, index + L(pattern))
                for index in (i for i, e in enumerate(row) if e == pattern[0])
                if row[index:index + L(pattern)] == pattern]


def checkio(pattern, image):
    N = len(pattern)
    d = {i: find(pattern[0], row) for i, row in enumerate(image)
         if find(pattern[0], row) != []}
    for k in d:
        for x in d[k]:
            a, b = x
            if [f[a:b] for f in image[k:k + N]] == pattern:
                for row in image[k:k + N]:
                    row[a:b] = map(lambda x: 2 if x == 0 else 3, row[a:b])
    return image

print checkio([[1, 0], [1, 1]],
              [[0, 1, 0, 1, 0],
               [0, 1, 1, 0, 0],
               [1, 0, 1, 1, 0],
               [1, 1, 0, 1, 1],
               [0, 1, 1, 0, 0]]) == [[0, 3, 2, 1, 0],
                                     [0, 3, 3, 0, 0],
                                     [3, 2, 1, 3, 2],
                                     [3, 3, 0, 3, 3],
                                     [0, 1, 1, 0, 0]]
print checkio([[1, 1], [1, 1]],
              [[1, 1, 1],
               [1, 1, 1],
               [1, 1, 1]]) == [[3, 3, 1],
                               [3, 3, 1],
                               [1, 1, 1]]

print checkio([[0, 1, 0], [1, 1, 1]],
              [[0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
               [0, 1, 1, 1, 0, 0, 0, 1, 1, 1],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
               [0, 1, 0, 0, 1, 1, 1, 0, 1, 0],
               [1, 1, 1, 0, 0, 0, 0, 0, 1, 1],
               [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
               [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
               [0, 1, 1, 0, 0, 0, 1, 1, 1, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]) == [[0, 2, 3, 2, 0, 0, 0, 2, 3, 2],
                                                    [0, 3, 3, 3, 0, 0, 0, 3, 3, 3],
                                                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                                    [0, 0, 0, 0, 2, 3, 2, 0, 0, 0],
                                                    [2, 3, 2, 0, 3, 3, 3, 0, 1, 0],
                                                    [3, 3, 3, 0, 0, 0, 0, 0, 1, 1],
                                                    [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
                                                    [0, 0, 1, 0, 0, 0, 2, 3, 2, 0],
                                                    [0, 1, 1, 0, 0, 0, 3, 3, 3, 0],
                                                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

# def find(pattern, row):
#     r = []
#     N = len(pattern)
#     for index in (i for i, e in enumerate(row) if e == pattern[0]):
#         if row[index:index + N] == pattern:
#             r.append((index, index + N))
#     [index for index in (i for i, e in enumerate(row) if e == pattern[0])
#      if row[index:index + N] == pattern]
#     return r
