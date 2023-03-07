# 바이러스

n = int(input())
m = int(input())

graph = [[0 for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    i, j = map(int, input().split())
    graph[i][j] = 1
    graph[j][i] = 1

# DFS

visited_dfs = [False] * (n + 1)
virus = []

def dfs(graph, v, visited):
    visited[v] = True
    for i in range(1, len(graph[v])):
        if graph[v][i] == 1 and visited[i] == False:
            virus.append(i)
            dfs(graph, i, visited)

dfs(graph, 1, visited_dfs)

print(len(virus))

# BFS

from collections import deque

visited_bfs = [False] * (n + 1)
virus = []

def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True
    while queue:
        start = queue.popleft()
        for i in range(1, len(graph[start])):
            if graph[start][i] == 1 and visited[i] == False:
                queue.append(i)
                visited[i] = True
                virus.append(i)

bfs(graph, 1, visited_bfs)
print(len(virus))

