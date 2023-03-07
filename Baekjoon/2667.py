# 단지번호붙이기

# BFS

from collections import deque

n = int(input())

graph = []

for _ in range(n):
    graph.append(list(map(int, input())))

visited = [[0 for _ in range(n)] for _ in range(n)]
count_list = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, g):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = g

    global count
    count += 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = g
                queue.append((nx, ny))
                count += 1
count = 0
group = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and visited[i][j] == 0:
            group += 1
            bfs(i, j, group)
            count_list.append(count)
            count = 0

print(group)

count_list.sort()

for i in range(len(count_list)):
    print(count_list[i])