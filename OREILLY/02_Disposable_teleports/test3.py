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
            edges.append((node, neighbour))
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


def checkio(teleports_string):
    print "Graph: %s" % graph(teleports_string)
    print "Edges: %s" % generate_edges(graph(teleports_string))
    print "Path: %s" % find_path(graph(teleports_string), '1', '5')

checkio("12,23,34,45,56,67,78,81")
