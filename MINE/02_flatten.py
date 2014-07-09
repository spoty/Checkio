import re

flatten=lambda l: sum(map(flatten,l),[]) if isinstance(l,list) else [l]

def flat_list(l):
    return [int(x) for x in re.sub(r'[\[,\]]', ' ', str(l)).split()]

def flat_list(l):
    return list(map(int, re.findall('-?\d+', str(l))))

def flat_list(l):
    r = []
    def f(l):
        for i in l:
            r.append(i) if type(i) is int else f(i)
    f(l)
    return r

flat_list=f=lambda d:0*d==0 and[d]or sum(map(f,d),[])

flat_list=lambda array: eval('['+str(array).translate(str.maketrans('','','[]'))+']')

f = lambda x: x and f(x[0]) + f(x[1:]) if isinstance(x, list) else [x]
flat_list = f

#regex
flat_list = lambda l: [int(x) for x in re.sub(r'[\[,\]]', ' ', str(l)).split()]

# replace
flat_list = lambda l: [int(x) for x in str(l).replace('[',' ').replace(']',' ').split(',')]

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
    if l==[]: return []
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
