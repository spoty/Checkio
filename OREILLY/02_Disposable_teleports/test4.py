import sys

A = {
    1: [2, 4],
    2: [1, 5],
    3: [4, 5],
    4: [1, 3, 5],
    5: [2, 3, 4],
    6: []
}

num_vertices = len(A)
sys.setrecursionlimit(num_vertices + 2)

mark = [None] * (num_vertices + 1)
cur_path = []

def DFS(vertex, cur_mark = 1):
    mark[vertex] = cur_mark
    global cur_path
    cur_path.append(vertex)
    for neighbour in A[vertex]:
        if not mark[neighbour]:
            DFS(neighbour, 3 - cur_mark)
        elif mark[neighbour] == cur_mark:
            print 'Found a loop of odd length: ', cur_path[cur_path.index(neighbour):]
            sys.exit(0)

    cur_path = cur_path[:-1]

# Visit all connected components
for vertex in xrange(1, len(A)):
    if not mark[vertex]:
        DFS(vertex)

print 'Cycle of odd length not found'
