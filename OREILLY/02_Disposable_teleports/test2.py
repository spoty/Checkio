def generate_edges(graph):
    edges = []
    for node in graph:
        for neighbour in graph[node]:
            edges.append((node, neighbour))
    return edges


def checkio(graph):
    mydict = {}
    listo = [e for e in graph.split(',')]
    for item in listo:
        if item[0] in mydict:
            mydict.setdefault(item[0], []).append(item[1])
        else:
            mydict[item[0]] = [item[1]]

    print "Graph: %s" % mydict
    print "Edges: %s" % generate_edges(mydict)


checkio("12,23,34,45,56,67,78,81")
checkio("12,28,87,71,13,14,34,35,45,46,63,65")
checkio("12,15,16,23,24,28,83,85,86,87,71,74 ,56")
checkio("13,14,23,25,34,35,47,56,58,76,68")
checkio("12,15,16,23,24,28,83,85,86,87,71,74,56")
