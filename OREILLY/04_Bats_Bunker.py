from math import sqrt


def Bresenham_supercover(x1, y1, x2, y2):
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
                    point.append((x, y-ystep))
                elif error + errorprev > ddx:
                    point.append((x-xstep, y))
                else:
                    point.append((x, y-ystep))
                    point.append((x-xstep, y))
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
                    point.append((x-xstep, y))
                elif error + errorprev > ddy:
                    point.append((x, y-ystep))
                else:
                    point.append((x-xstep, y))
                    point.append((x, y-ystep))
            point.append((x, y))
            errorprev = error
            i += 1
    return point


def dijkstra(net, s, t):
    if s == t:
        return "The start and terminal nodes are the same."
    if not s in net:
        return "There is no start node called " + str(s) + "."
    if not t in net:
        return "There is no terminal node called " + str(t) + "."
    # create a labels dictionary
    labels = {}
    # record whether a label was updated
    order = {}
    # populate an initial labels dictionary
    for i in net.keys():
        if i == s:
            labels[i] = 0  # shortest distance form s to s is 0
        else:
            labels[i] = float("inf")  # initial labels are infinity
    from copy import copy
    drop1 = copy(labels)  # used for looping
    # begin algorithm
    while len(drop1) > 0:
        # find the key with the lowest label
        # minNode is the node with the smallest label
        minNode = min(drop1, key=drop1.get)
        # update labels for nodes that are connected to minNode
        for i in net[minNode]:
            if labels[i] > (labels[minNode] + net[minNode][i]):
                labels[i] = labels[minNode] + net[minNode][i]
                drop1[i] = labels[minNode] + net[minNode][i]
                order[i] = minNode
        # once a node has been visited, it's excluded from drop1
        del drop1[minNode]
    # end algorithm
    # print shortest path
    temp = copy(t)
    rpath = []
    path = []
    while 1:
        rpath.append(temp)
        if temp in order:
            temp = order[temp]
        else:
            return "There is no path from " + str(s) + " to " + str(t) + "."
        if temp == s:
            rpath.append(temp)
            break
    for j in range(len(rpath) - 1, -1, -1):
        path.append(rpath[j])
    return float(("%.2f" % labels[t]))


def just_straight_lines(lines_of_sight, walls):
    return [line for line in lines_of_sight if not any(wall in walls for wall in line)]


def just_edges(straight_lines):
    edges = []
    for line in straight_lines:
        if len(line) != 1:
            edges.append(line[::len(line) - 1])
    return edges


def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = sqrt(
        (node1[0] - node2[0]) ** 2 + (node1[1] - node2[1]) ** 2)
    return G


def make_graph(link_list):
    G = dict()
    for n1, n2 in link_list:
        make_link(G, n1, n2)
    return G


def checkio(string):
    # Get grid dimensions
    map_x = len(string[0])
    map_y = len(string)
    # Initiate GRID
    if map_x == map_y:
        bunker = [(string[x][y], x + 0.5, y + 0.5)
                  for x in range(map_x) for y in range(map_y)]
    if map_x > map_y:
                bunker = [(string[y][x], x + 0.5, y + 0.5) for x in range(map_x) for y in range(map_y)]
    # Bats + Alfa
    bats = [x for x in bunker if x[0] == "B" or x[0] == "A"]
    # Walls
    walls = [x[1:] for x in bunker if x[0] == "W"]
    # Lines of sight
    lines_of_sight = [(Bresenham_supercover(from_bat[1], from_bat[2], to_bat[1], to_bat[2]))
                      for from_bat in bats for to_bat in bats]
    # Get coordinates for Alfa Bet
    for x in bunker:
        if x[0] == "A":
            alpha_X = x[1]
            alpha_Y = x[2]
    if alpha_X == 0.5 and alpha_Y == 0.5:
        return 0
    # Get lines without obstacles
    clear_view = just_straight_lines(lines_of_sight, walls)
    # Get edges
    edges = just_edges(clear_view)
    # Create Graph with weights
    Graph = make_graph(edges)
    # Call Dijkstra
    return dijkstra(Graph, (0.5, 0.5), (alpha_X, alpha_Y))


print checkio([
    "B--",
    "---",
    "--A"])

print checkio([
    "B-B",
    "BW-",
    "-BA"])

print checkio(["B--", "---", "--A"])

print checkio([
    "B---B-",
    "-WWW-B",
    "-WA--B",
    "-W-B--",
    "-WWW-B",
    "B-BWB-"])

print checkio([
    "BWB--B",
    "-W-WW-",
    "B-BWAB"])
