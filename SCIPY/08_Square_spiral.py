import heapq
import math
import random

def manhattan_h(goal):
   def f(pos):
       dx, dy = pos.x - goal.x, pos.y - goal.y
       return abs(dx) + abs(dy)
   return f

def build_path(start, finish, parent):
    """
    Reconstruct the path from start to finish given
    a dict of parent links.

    """
    x = finish
    xs = [x]
    while x != start:
        x = parent[x]
        xs.append(x)
    xs.reverse()
    return xs

def solve(start, finish, heuristic):
    """Find the shortest path from START to FINISH."""
    heap = []

    link = {} # parent node link
    h = {} # heuristic function cache
    g = {} # shortest path to a node

    g[start] = 0
    h[start] = 0
    link[start] = None


    heapq.heappush(heap, (0, 0, start))
    # keep a count of the  number of steps, and avoid an infinite loop.
    for kk in xrange(1000000):
        f, junk, current = heapq.heappop(heap)
        if current == finish:
            # print "distance:", g[current], "steps:", kk
            # return g[current], kk, build_path(start, finish, link)
            return g[current]

        moves = current.get_moves()
        distance = g[current]
        for mv in moves:
            if mv not in g or g[mv] > distance + 1:
                g[mv] = distance + 1
                if mv not in h:
                    h[mv] = heuristic(mv)
                link[mv] = current
                heapq.heappush(heap, (g[mv] + h[mv], -kk, mv))
    else:
        raise Exception("did not find a solution")


class GridPosition(object):
    """Represent a position on a grid."""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash((self.x, self.y))

    def __repr__(self):
        return "GridPosition(%d,%d)" % (self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def get_moves(self):
        # There are times when returning this in a shuffled order
        # would help avoid degenerate cases.  For learning, though,
        # life is easier if the algorithm behaves predictably.
        yield GridPosition(self.x + 1, self.y)
        yield GridPosition(self.x, self.y + 1)
        yield GridPosition(self.x - 1, self.y)
        yield GridPosition(self.x, self.y - 1)

def spiral(X, Y):
    graph = {}
    x = y = 0
    dx, dy = 0, 1
    for i in range(1,max(X, Y)**2):
        if (-X/2 < x <= X/2) and (-Y/2 < y <= Y/2): # in case of N x M
            graph[i]=(x,y)
        if (x <= 0 and y == 1-x) or (x==y and (x!=0 and y!=0)) or (y<0 and x==-y):
            dx, dy = dy, -dx
        x, y = x+dx, y+dy
    return graph


def checkio(n,m):
    graph = spiral(100,100)
    print graph[n], graph[m]
    grid_start = GridPosition(graph[n][0],graph[n][1])
    grid_end = GridPosition(graph[m][0],graph[m][1])
    return solve(grid_start, grid_end, manhattan_h(grid_end))

print checkio(10,25)
