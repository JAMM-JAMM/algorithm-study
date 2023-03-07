# 토마토

from collections import deque

m, n = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

queue = deque()

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append((j, i))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue:
    x, y = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= m or ny >= n:
            continue
            
        if graph[ny][nx] == -1:
            continue

        if graph[ny][nx] == 0:
            graph[ny][nx] = graph[y][x] + 1
            queue.append((nx, ny))

answer = 0
flag = False

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            print(-1)
            flag = True
            break
        elif graph[i][j] != 0 and graph[i][j] != -1:
            answer = max(answer, graph[i][j])
    
    if flag:
        break

if not flag:
    print(answer-1)