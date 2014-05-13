def graph(graph):
    mydict = {}
    listo = [e for e in graph.split(',')]
    for item in listo:
        if item[0] in mydict:
            mydict.setdefault(item[0], []).append(item[1])
        else:
            mydict[item[0]] = [item[1]]

    return mydict


def generate_edges(graph):
    edges = []
    for node in graph:
        for neighbour in graph[node]:
            edges.append((int(node), int(neighbour)))
    return edges

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
    path = []
    if len(graph) == 0:
        if node_start is None:
            return []
        return [node_start]

    node_start = graph[0][0] if node_start is None else node_start

    for chosen_edge in [x for x in graph if node_start in x]:
        (node_a, node_b) = chosen_edge
        path = take_tour([e for e in graph if e != chosen_edge],
                         node_b if node_start == node_a else node_a,
                         cycle_only=False)

        if path is not False and (not cycle_only or node_start == path[-1]):
            # if all(str(x) in GOAL for x in path):
            #     return [node_start] + path + ['XX']
            return [node_start] + path
    return False

def checkio(teleports_string):
    take_tour([(0, 1), (1, 5), (1, 7), (4, 5), (4, 8), (1, 6),
               (3, 7), (5, 9), (2, 4), (0, 4), (2, 5), (3, 6), (8, 9)])

print checkio("12,23,34,45,56,67,78,81")
