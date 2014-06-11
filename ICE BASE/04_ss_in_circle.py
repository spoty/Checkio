from math import pi, floor, sqrt


def checkio(radius):
    N = 1  # square tile has size of 1x1 meters

    upper_limit = int(floor((pi*(radius**2))/(N*N)))
    lower_limit = int(floor((sqrt(2)*radius)/N)**2)

    return [lower_limit, upper_limit]

from math import sqrt,ceil

# def checkio(radius):
#     tiles = partial = 0
#     left_height = radius
#     length = int(ceil(radius))
#     square_radius = radius**2
#     for x in range(1, length):
#         height = sqrt(square_radius - x**2)
#         tiles += int(height)
#         partial += int(ceil(left_height)) - int(height)
#         left_height = height
#     partial += int(ceil(left_height))
#     return [tiles*4, partial*4]


# from itertools import product
# from math import hypot, ceil

# def checkio(radius):
#     whole, partial = 0, 0
#     for x0, y0 in product(range(ceil(radius)), repeat=2):
#         if hypot(x0, y0) < radius:
#             x1, y1 = x0 + 1, y0 + 1
#             if hypot(x1, y1) <= radius:
#                 whole += 4
#             else:
#                 partial += 4
#     return [whole, partial]

print checkio(2)
print checkio(3)
print checkio(2.1)
print checkio(2.5)
