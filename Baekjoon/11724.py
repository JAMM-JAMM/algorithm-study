# 연결 요소의 개수

import sys
from collections import deque

sys.setrecursionlimit(10000) # DFS의 경우 recursion error를 방지하기 위해 

input = sys.stdin.readline
n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# visited_bfs = [False for _ in range(n+1)]
visited_dfs = [False for _ in range(n+1)]

# def bfs(v):
#     queue = deque()
#     queue.append(v)
#     while queue:
#         start = queue.popleft()
#         visited_bfs[start] = True
#         for i in graph[start]:
#             if visited_bfs[i] == False:
#                 queue.append(i)
#                 visited_bfs[i] = True

def dfs(v):
    visited_dfs[v] = True
    for i in graph[v]:
        if visited_dfs[i] == False:
            visited_dfs[i] = True
            dfs(i)

count = 0

# for i in range(1, n+1):
#     if visited_bfs[i] == False:
#         bfs(i)
#         count += 1

for j in range(1, n+1):
    if visited_dfs[j] == False:
        dfs(j)
        count += 1

print(count)
