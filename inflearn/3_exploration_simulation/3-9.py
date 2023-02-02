'''
봉우리

풀이 날짜 : 2023-02-01
풀이 소요 시간 : 풀이 참조
'''

import sys


sys.stdin = open("input.txt", "r")
n = int(input())
n_mat = [list(map(int, input().split())) for _ in range(n)]

n_mat.insert(0, [0]*n)
n_mat.append([0]*n)

for row in n_mat:
    row.insert(0, 0)
    row.append(0)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

cnt = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        if all(n_mat[i][j] > n_mat[i + dx[k]][j + dy[k]] for k in range(4)):
            cnt += 1

print(cnt)