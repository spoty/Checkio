def num2pos(num, size):
    x, y = divmod(num, size)
    return x, y


def checkio(lines_list):
    """Return the quantity of squares"""

    for line in lines_list:
        line.sort()
    lines_list.sort()

    count = 0
    size = 4

    for line in lines_list:
        start, end = line
        if end - start != 1:
            continue

        x, y = num2pos(start, size)
        ith = 1

        while ith + y <= size:
            # one step right
            if [start + ith - 1, start + ith] not in lines_list:
                break
            end = start + ith
            # right down from right top
            flag = False
            for i in range(1, ith + 1):
                if [end + (i - 1) * size, end + i * size] not in lines_list:
                    # not connected in the middle
                    flag = True
                    break
            # 2 -> 6 is not connected in graph two, but 4 -> 8 is connected
            if flag:
                ith += 1
                continue
            # left from right bottom
            flag = False
            for i in range(ith, 0, -1):
                if [end + size * ith - 1, end + size * ith] not in lines_list:
                    # not connected in the middle
                    flag = True
                    break
                end = end - 1
            # see above
            if flag:
                ith += 1
                continue
            # one step up back from left bottom
            if [start + size * (ith - 1), start + size * ith] not in lines_list:
                break
            ith += 1
            count += 1
    return count


print checkio([[1, 2], [3, 4], [1, 5], [2, 6], [4, 8], [5, 6], [6, 7],
     [7, 8], [6, 10], [7, 11], [8, 12], [10, 11],
     [10, 14], [12, 16], [14, 15], [15, 16]])

# print checkio([[1, 2], [2, 3], [3, 4], [1, 5], [4, 8],
#      [6, 7], [5, 9], [6, 10], [7, 11], [8, 12],
#      [9, 13], [10, 11], [12, 16], [13, 14], [14, 15], [15, 16]])
