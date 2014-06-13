# # http://stackoverflow.com/questions/13435413/python-code-to-find-eulerian-tour-does-not-work-in-one-case-why
# # Eulerian Path/Circuit
# GOAL = "12345678"

def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath:
                return newpath
    return None

def take_tour(graph, node_start=1, cycle_only=True):
    GOAL = "12345678"
    if len(graph) == 0:
        if node_start is None:
            return []
        return [node_start]
    path = []
    node_start = graph[0][0] if node_start is None else node_start
    for chosen_edge in [x for x in graph if node_start in x]:
        (node_a, node_b) = chosen_edge
        path = take_tour([e for e in graph if e != chosen_edge],
                         node_b if node_start == node_a else node_a,
                         cycle_only=True)
        if path is not False and (all(str(x) in GOAL for x in path)):
            return [node_start] + path
        if path is not False and (not cycle_only or node_start == path[-1]):
            return [node_start] + path
    return path

def checkio(teleports_string):
    graph = [(int(item[0]), int(item[1])) for item in [e for e in teleports_string.split(',')]]
    rez = take_tour(graph)

    # return "".join(str(x) for x in rez)
    return rez


print checkio("12,23,34,45,56,67,78,81")
print checkio("12,28,87,71,13,14,34,35,45,46,63,65")
print checkio("12,15,16,23,24,28,83,85,86,87,71,74,56")

# print checkio([(1, 2), (1, 5), (1, 6), (8, 3), (8, 5), (8, 6),
#                 (8, 7), (2, 3), (2, 4), (2, 8), (5, 6), (7, 1), (7, 4)])

# print checkio([(1, 3), (1, 4), (3, 4), (3, 5), (2, 3),
#                (2, 5), (5, 6), (5, 8), (4, 7), (7, 6), (6, 8)])

# print checkio([(1, 2), (3, 4), (2, 3), (5, 6), (4, 5), (7, 8), (6, 7), (8, 1)])


# def find_path(graph, start ='1', end='1', path=[]):
#     if start != '1':
#         path = path + [start]
#     if not graph.has_key(start):
#         return None
#     for node in graph[start]:
#         if node not in path:
#             newpath = find_path(graph, node, end, path)
#             if newpath: return newpath

#     if start == end:
#         return ['1'] + path + ['1']
#     return None

# def checkio(teleports_string):
#     mydict = {}
#     for item in [e for e in teleports_string.split(',')]:
#         if item[0] in mydict:
#             mydict.setdefault(item[0], []).append(item[1])
#         else:
#             mydict[item[0]] = [item[1]]
#     print mydict
#     return ''.join((find_path(mydict)))


# print checkio("12,23,34,45,56,67,78,81")
# print checkio("12,28,87,71,13,14,34,35,45,46,63,65")
# print checkio("12,15,16,23,24,28,83,85,86,87,71,74,56")

# def checkio(teleports_string):

#     print [(int(item[0]), int(item[1])) for item in [e for e in teleports_string.split(',')]]

#     # print mydict


# print checkio("13,14,23,25,34,35,47,56,58,76,61")
