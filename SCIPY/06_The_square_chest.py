import itertools


def S(A):
    """
    Function S takes a list of complex numbers as its input (A). If we know both
    the centre and one corner of a square, we can reconstruct the square by
    rotating the corner 90,180 and 270 degrees around the centre point (c). On
    the complex plane rotation by 90 degrees about the origin is done by
    multiplying the point by i. If our original shape and the reconstructed
    square have the same points then it must have been a square.
    """
    c=sum(A)/4.0
    return set(A)==set((A[0]-c)*1j**i+c for i in range(4))

def checkio(lines):

    count = 0
    size = 4

    def num2pos(num, size):
        x, y = divmod(num-1,size)
        return [x, y]

    coords = []
    for line in lines:
        start, end = line
        coords.append(num2pos(start, size))
        coords.append(num2pos(end, size))

    coords.sort()
    coords = list(coords for coords,_ in itertools.groupby(coords))
    c = [complex(x[0], x[1]) for x in coords]


    for x in itertools.combinations(c, 4):
        if S(x):
            count += 1
            print x
    return count


l = [[1, 2], [3, 4], [1, 5], [2, 6], [4, 8], [5, 6], [6, 7],
     [7, 8], [6, 10], [7, 11], [8, 12], [10, 11],
     [10, 14], [12, 16], [14, 15], [15, 16]]
print checkio(l)
