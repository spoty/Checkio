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
    def heuristic(graph):
        dx = abs(graph[n][0] - graph[m][0])
        dy = abs(graph[n][1] - graph[m][1])
        return (dx + dy)
    return heuristic(graph)

print checkio(9,1)
