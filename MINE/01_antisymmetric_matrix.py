# def checkio(matrix):
#     return [[-e for e in i] for i in matrix] == [list(i) for i in zip(*matrix)]

# checkio = lambda m: [[-e for e in i] for i in m] == [list(i) for i in zip(*m)]

checkio = lambda m: m == [[-e for e in i] for i in zip(*m)]

print checkio([
    [0, 1, 2],
    [-1, 0, 1],
    [-2, -1, 0]])
print checkio([
    [0, 1, 2],
    [-1, 1, 1],
    [-2, -1, 0]])
print checkio([
    [0, 1, 2],
    [-1, 0, 1],
    [-3, -1, 0]])
