# 숨바꼭질

from collections import deque


n, k = map(int, input().split())
m = 10 ** 5
distance = [0 for _ in range(m+1)]

def bfs():
    queue = deque()
    queue.append(n)
    while queue:
        x = queue.popleft()
        if x == k:
            print(distance[x])
            break
        for nx in (x-1, x+1, x*2):
            if 0 <= nx <= m and not distance[nx]:
                distance[nx] = distance[x] + 1
                queue.append(nx)

bfs()