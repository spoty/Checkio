import re


def flat_list(l):
    return [int(x) for x in re.sub(r'[\[,\]]', ' ', str(l)).split()]

# regex
flat_list = lambda l: [int(x) for x in re.sub(r'[\[,\]]', ' ', str(l)).split()]

# replace
flat_list = lambda l: [int(x) for x in str(l).replace('[', ' ').replace(']', ' ').split(',')]

# recursive - generator


def flat_list(l):
    for item in l:
        try:
            for i in flat_list(item):
                yield i
        except TypeError:
            yield item

# recursive


def flat_list(l):
    if l == []:
        return []
    elif type(l) != list:
        return [l]
    else:
        a = flat_list(l[0])
        b = flat_list(l[1:])
        a.extend(b)
        return a


# print flat_list([1, 2, 3]) == [1, 2, 3]
# print flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4]
print flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]])
# print flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1]
