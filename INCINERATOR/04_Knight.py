"""
Input: Squares coordinates as a string.

Output: The number of moves in the shortest path the knight can take as an
integer.
"""
import collections


def checkio(cells):
    s, e = cells.split('-')
    m =  [[x+y for x in "abcdefgh"] for y in "12345678"]
    board = collections.defaultdict(set)

    for x in range(0,8):
        for y in range(0,8):
            K = [[x+1, y+2],[x+1, y-2],[x+2, y+1],[x+2, y-1],
                [x-1, y+2],[x-1, y-2],[x-2, y+1],[x-2, y-1]]
            [board[m[x][y]].add(m[a][b]) for a,b in [p for p in K]
                                            if 8>a>0 and 8>b>0]

    def bfs_paths(graph, start, goal):
        queue = [(start, [start])]
        while queue:
            (vertex, path) = queue.pop(0)
            for next in graph[vertex] - set(path):
                if next == goal:
                    yield path + [next]
                else:
                    queue.append((next, path + [next]))

    def shortest_path(graph, start, goal):
        try:
            return next(bfs_paths(graph, start, goal))
        except StopIteration:
            return None

    # print next(bfs_paths(board, s, e))
    return len(shortest_path(board, s, e))-1

print checkio(u"b1-d5") == 2
print checkio(u"a6-b8") == 1
print checkio(u"h1-g2") == 4
print checkio(u"h8-d7") == 3
print checkio(u"a1-h8") == 6
print checkio(u"e2-e3")
