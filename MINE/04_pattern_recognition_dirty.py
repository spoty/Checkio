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


# def find(haystack, needle):
#     """Return the index at which the sequence needle appears in the
#     sequence haystack, or -1 if it is not found, using the Boyer-
#     Moore-Horspool algorithm. The elements of needle and haystack must
#     be hashable.

#     >>> find([1, 1, 2], [1, 2])
#     1

#     """
#     h = len(haystack)
#     n = len(needle)
#     skip = {needle[i]: n - i - 1 for i in range(n - 1)}
#     i = n - 1
#     while i < h:
#         for j in range(n):
#             if haystack[i - j] != needle[-j - 1]:
#                 i += skip.get(haystack[i], n)
#                 break
#         else:
#             return (i - n + 1), (i - n + 1) + 3
#     return 0


# def checkio(pattern, image):
#     N = len(pattern)

#     for i, row in enumerate(image):
#             for p in range(N):
#                 if find(row, pattern[0]) != 0:
#                     a, b = find(row, pattern[0])
#                     if [f[a:b] for f in image[i:i + N] if a + b > 0] == pattern:
#                         for row2 in image[i:i + N]:
#                             row2[a:b] = map(lambda x: 2 if x == 0 else 3, row2[a:b])
#     print "\n".join(str(x) for x in image)
#     return image

def find(sl,l):
    results=[]
    sll=len(sl)
    for ind in (i for i,e in enumerate(l) if e==sl[0]):
        if l[ind:ind+sll]==sl:
            results.append((ind,ind+sll))
    return results

def checkio(pattern, image):
    N = len(pattern)
    # print find(pattern[0], image[0])
    d = {i:find(pattern[0], row) for i,row in enumerate(image)
                                 if find(pattern[0], row) != []}
    print "\n".join(str(x) for x in image)
    print d
    for k in d:
        # print image[k:k+N]
        #if [f[d[k][0]:d[k][1]] for f in image[k:k+N]] == pattern
        # print [f[d[k][0]:d[k][1]] for f in image[k:k+N]]
        for x in d[k]:
            a, b = x
            print a,b
            # print [f[a:b] for f in image[k:k+N]], pattern
            if [f[a:b] for f in image[k:k+N]] == pattern:
                for row in image[k:k+N]:
                    row[a:b] = map(lambda x: 2 if x == 0 else 3, row[a:b])

    print "\n".join(str(x) for x in image)






    # print "\n".join(str(x) for x in image)
    return image

# print checkio([[1, 0], [1, 1]],
#         [[0, 1, 0, 1, 0],
#          [0, 1, 1, 0, 0],
#          [1, 0, 1, 1, 0],
#          [1, 1, 0, 1, 1],
#          [0, 1, 1, 0, 0]]) == [[0, 3, 2, 1, 0],
#                                [0, 3, 3, 0, 0],
#                                [3, 2, 1, 3, 2],
#                                [3, 3, 0, 3, 3],
#                                [0, 1, 1, 0, 0]]
# print checkio([[1, 1], [1, 1]],
#         [[1, 1, 1],
#          [1, 1, 1],
#          [1, 1, 1]]) == [[3, 3, 1],
#                          [3, 3, 1],
#                          [1, 1, 1]]

print checkio([[0,1,0],[1,1,1]],
       [[0,0,1,0,0,0,0,0,1,0],
        [0,1,1,1,0,0,0,1,1,1],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,1,0,0,0,0],
        [0,1,0,0,1,1,1,0,1,0],
        [1,1,1,0,0,0,0,0,1,1],
        [0,0,0,1,1,1,0,0,0,0],
        [0,0,1,0,0,0,0,1,0,0],
        [0,1,1,0,0,0,1,1,1,0],
        [0,0,0,0,0,0,0,0,0,0]]) == [[0,2,3,2,0,0,0,2,3,2],[0,3,3,3,0,0,0,3,3,3],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,2,3,2,0,0,0],[2,3,2,0,3,3,3,0,1,0],[3,3,3,0,0,0,0,0,1,1],[0,0,0,1,1,1,0,0,0,0],[0,0,1,0,0,0,2,3,2,0],[0,1,1,0,0,0,3,3,3,0],[0,0,0,0,0,0,0,0,0,0]]
