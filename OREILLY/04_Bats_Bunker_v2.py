from math import sqrt, hypot


def Bresenham_supercover(x1, y1, x2, y2):
    """http://lifc.univ-fcomte.fr/home/~ededu/projects/bresenham/"""
    x, y = x1, y1
    dx, dy = x2 - x1, y2 - y1
    point = [(x1, y1)]
    i = 0
    if dy < 0:
        ystep = -1
        dy = -dy
    else:
        ystep = 1

    if dx < 0:
        xstep = -1
        dx = -dx
    else:
        xstep = 1

    ddy, ddx = 2 * dy, 2 * dx

    if ddx >= ddy:
        errorprev, error = dx, dx
        while i < dx:
            x += xstep
            error += ddy
            if error > ddx:
                y += ystep
                error -= ddx
                if error + errorprev < ddx:
                    point.append((x, y - ystep))
                elif error + errorprev > ddx:
                    point.append((x - xstep, y))
                else:
                    point.append((x, y - ystep))
                    point.append((x - xstep, y))
            point.append((x, y))
            errorprev = error
            i += 1
    else:
        errorprev = error = dy
        while i < dy:
            y += ystep
            error += ddx
            if error > ddy:
                x += xstep
                error -= ddy
                if error + errorprev < ddy:
                    point.append((x - xstep, y))
                elif error + errorprev > ddy:
                    point.append((x, y - ystep))
                else:
                    point.append((x - xstep, y))
                    point.append((x, y - ystep))
            point.append((x, y))
            errorprev = error
            i += 1
    return point


def Dijkstra(net, s, t):
    """http://en.wikipedia.org/wiki/Dijkstra%27s_algorithm"""
    if s not in net:
        raise NameError("There is no start node {}.".format(s))
    if t not in net:
        raise NameError("There is no end node {}.".format(t))
    dist = {}
    for i in net:
        if i == s:
            dist[i] = 0  # shortest distance form s to s is 0
        else:
            dist[i] = float("inf")  # initial dist are infinity
    temp = dist.copy()
    while temp:
        minN = min(temp, key=temp.get)
        # update dist for nodes that are connected to minN
        for i in net[minN]:
            if dist[i] > (dist[minN] + net[minN][i]):
                dist[i] = dist[minN] + net[minN][i]
                temp[i] = dist[minN] + net[minN][i]
        # once a node has been visited, it's excluded from temp
        del temp[minN]
    # end algorithm
    return round(dist[t], 2)


def just_straight_lines(lines_of_sight, walls):
    return [line for line in lines_of_sight if not any(wall in walls for wall in line)]


def just_edges(straight_lines):
    edges = []
    for i, line in enumerate(straight_lines):
        if len(line) == 1:
            edges.append(line)
            edges[i].append(line[0])
        else:
            edges.append(line[::len(line) - 1])
    return edges


def make_graph(link_list):
    G = {}
    def make_link(node1, node2):
        if node1 not in G:
            G[node1] = {}
        (G[node1])[node2] = hypot((node1[0] - node2[0]), (node1[1] - node2[1]))
    for n1, n2 in link_list:
        make_link(n1, n2)
    return G


def checkio(mapa):
    # Initiate GRID
    bunker = [(char, x+.5, y+.5) for y, row in enumerate(mapa)
                                 for x, char in enumerate(row)]
    # Bats + Alfa
    bats = [x for x in bunker if x[0] in "AB"]
    # Walls
    walls = [x[1:] for x in bunker if x[0] == "W"]
    # walls = [c for char, *c in bunker if char == "W"]
    # Lines of sight
    lines_of_sight = [(Bresenham_supercover(from_bat[1], from_bat[2], to_bat[1], to_bat[2]))
                      for from_bat in bats
                      for to_bat in bats]
    # Get lines without obstacles
    clear_view = just_straight_lines(lines_of_sight, walls)
    # Get edges
    edges = just_edges(clear_view)
    # Create Graph with weights
    Graph = make_graph(edges)
    # Get coordinates for Alfa Bet
    for x in bunker:
        if x[0] == "A":
            alpha_X = x[1]
            alpha_Y = x[2]
    # Call Dijkstra
    return Dijkstra(Graph, (0.5, 0.5), (alpha_X, alpha_Y))


print checkio([
    "B--",
    "---",
    "--A"])

print checkio([
    "A--",
    "---",
    "---"])

# print checkio([
#     "B-B",
#     "BW-",
#     "-BA"])

# print checkio(["B--", "---", "--A"])

# print checkio([
#     "B---B-",
#     "-WWW-B",
#     "-WA--B",
#     "-W-B--",
#     "-WWW-B",
#     "B-BWB-"])

# print checkio([
#     "BWB--B",
#     "-W-WW-",
#     "B-BWAB"])
