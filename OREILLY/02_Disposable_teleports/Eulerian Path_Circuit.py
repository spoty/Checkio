# http://stackoverflow.com/questions/13435413/python-code-to-find-eulerian-tour-does-not-work-in-one-case-why
# Eulerian Path/Circuit
GOAL = "12345678"

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

def take_tour(graph, node_start=1, cycle_only=False):
    GOAL = "12345678"
    if len(graph) == 0:
        if node_start is None:
            return []
        return [node_start]

    node_start = graph[0][0] if node_start is None else node_start
    # print "Edges: %s" % [x for x in graph if node_start in x]
    for chosen_edge in [x for x in graph if node_start in x]:
        (node_a, node_b) = chosen_edge
        path = take_tour([e for e in graph if e != chosen_edge],
                         node_b if node_start == node_a else node_a,
                         cycle_only=False)
        if path is not False and (all(str(x) in GOAL for x in path)):
            return [node_start] + path + ['XX']
        if path is not False and (not cycle_only or node_start == path[-1]):
            return [node_start] + path
    return False


print take_tour([(0, 1), (1, 5), (1, 7), (4, 5), (4, 8), (1, 6),
               (3, 7), (5, 9), (2, 4), (0, 4), (2, 5), (3, 6), (8, 9)])

print take_tour([(1, 2), (1, 5), (1, 6), (8, 3), (8, 5), (8, 6),
                (8, 7), (2, 3), (2, 4), (2, 8), (5, 6), (7, 1), (7, 4)])

print take_tour([(1, 3), (1, 4), (3, 4), (3, 5), (2, 3),
               (2, 5), (5, 6), (5, 8), (4, 7), (7, 6), (6, 8)])

print take_tour([(1, 2), (3, 4), (2, 3), (5, 6), (4, 5), (7, 8), (6, 7), (8, 1)])

