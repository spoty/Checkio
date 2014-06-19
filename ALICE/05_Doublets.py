import collections

def linked(a, b):
    return len([i for i in range(3) if str(a)[i] == str(b)[i]]) == 2

def checkio(k):
    seq = collections.defaultdict(set)
    [seq[num].add(num2) for num in k for num2 in k if linked(num,num2)]


    def dfs_paths(graph, start, goal):
        stack = [(start, [start])]
        while stack:
            (vertex, path) = stack.pop()
            for next in graph[vertex] - set(path):
                if next == goal:
                    yield path + [next]
                else:
                    stack.append((next, path + [next]))

    f = list(dfs_paths(seq, k[0], k[-1]))
    return [x for x in f if len(x) == min(map(len, f))][0]


print checkio([123, 991, 323, 321, 329, 121, 921, 125, 999]) == [123, 121, 921, 991, 999]
print checkio([111, 222, 333, 444, 555, 666, 121, 727, 127, 777]) == [111, 121, 127, 727, 777]
print checkio([456, 455, 454, 356, 656, 654]) == [456, 454, 654]
