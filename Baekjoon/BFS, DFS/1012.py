# 유기농 배추

# DFS (런타임 에러..?)

# t = int(input())

# answer = []

# def dfs(x, y):
#     if x < 0 or x >= n or y < 0 or y >= m:
#         return 0
    
#     if graph[x][y] == 1:
#         graph[x][y] = 2
#         dfs(x-1, y)
#         dfs(x, y-1)
#         dfs(x+1, y)
#         dfs(x, y+1)
#         return 1
    
#     return 0

# for _ in range(t):

#     m, n, k = map(int, input().split())

#     count = 0

#     graph = []

#     for i in range(n):
#         graph.append([0 for j in range(m)])
    
#     for _ in range(k):
#         x ,y = map(int, input().split())
#         graph[y][x] = 1
    
#     for i in range(n):
#         for j in range(m):
#             if dfs(i, j) == 1:
#                 count += 1
    
#     answer.append(count)

# for i in range(len(answer)):
#     print(answer[i])
    
# BFS

from collections import deque


t = int(input())

answer = []

def bfs(x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                if graph[nx][ny] == 1:
                    queue.append((nx, ny))
                    graph[nx][ny] = 2


for _ in range(t):

    m, n, k = map(int, input().split())

    count = 0

    graph = []

    for i in range(n):
        graph.append([0 for j in range(m)])
    
    for _ in range(k):
        x ,y = map(int, input().split())
        graph[y][x] = 1
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                bfs(i, j)
                count += 1
    
    answer.append(count)

for i in range(len(answer)):
    print(answer[i])