def checkio(matrix):
    """ This Function Transpose matrix
    """
    # 1 For N x N cases
    print [col for x ,row in enumerate(matrix)
                   for y, col in enumerate(row)]
    # 2 Valid for N x N and N x M
    # return [list(i) for i in zip(*matrix)]

    # return list(zip(*matrix))

print checkio([[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]])

# print checkio([[1, 4, 3],
#          [8, 2, 6],
#          [7, 8, 3],
#          [4, 9, 6],
#          [7, 8, 1]])

# Numpy transpose
# import numpy as np
# a = np.array([(1,2,3), (4,5,6)])
# b = a.transpose()

# uneven = [['a','b','c'],['d','e'],['g','h','i']]
# >>> map(None,*uneven)
# [('a', 'd', 'g'), ('b', 'e', 'h'), ('c', None, 'i')]
