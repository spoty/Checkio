def mydict(string):
    mydict = {}
    listo = [e for e in string.split(',')]
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

def find_tour(u,E,tour):
    for (a,b) in E:
        print E
        print u
        print (a, b)
        if a==u:
            E.remove((a,b))
            find_tour(b,E,tour)
        elif b==u:
            E.remove((a,b))
            find_tour(a,E,tour)
    # if tour[0] != u:
    print tour
    tour.insert(0,u)

def checkio(string):
    tour=[]

    find_tour(generate_edges(mydict(string))[0][0],generate_edges(mydict(string)),tour)
    # print generate_edges(mydict(string))
    return ''.join(tour).strip()


# print checkio("12,23,34,45,56,67,78,81")
# print checkio("12,28,87,71,13,14,34,35,45,46,63,65")
# print checkio("12,15,16,23,24,28,83,85,86,87,71,74,56")
# print checkio("13,14,23,25,34,35,47,56,58,76,68")
# print checkio("12,15,16,23,24,28,83,85,86,87,71,74,56")
print checkio("13,14,23,25,34,35,47,56,58,76,68")
