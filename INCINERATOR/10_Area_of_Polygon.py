"""
A=1/2(|x_1 x_2; y_1 y_2|+|x_2 x_3; y_2 y_3|+...+|x_n x_1; y_n y_1|)
"""

def checkio(data):
    pairs = lambda p: zip(p, p[1:] + [p[0]])
    return 0.5 * abs(sum(x_1*y_2 - x_2*y_1
                         for ((x_1, y_1), (x_2, y_2)) in pairs(data)))




print checkio([[1, 1], [9, 9], [9, 1]])
print checkio([[4, 10], [7, 1], [1, 4]])
