# DFS와 BFS

n, m, v = map(int, input().split())

graph = []

for _ in range(n+1):
    graph.append([0 for _ in range(n+1)])

for _ in range(m):
    i, j = map(int, input().split())
    graph[i][j] = 1
    graph[j][i] = 1

# DFS

visited_dfs = [False] * (n + 1)

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in range(1, len(graph[v])):
        if graph[v][i] == 1 and visited[i] == False:
            dfs(graph, i, visited)

dfs(graph, v, visited_dfs)
print()

# BFS

from collections import deque

visited_bfs = [False] * (n + 1)

def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True
    while queue:
        start = queue.popleft()
        print(start, end=' ')
        for i in range(1, len(graph[start])):
            if graph[start][i] == 1 and visited[i] == False:
                queue.append(i)
                visited[i] = True

bfs(graph, v, visited_bfs)