'''
사과나무(다이아몬드)

풀이 날짜 : 2023-02-01
풀이 소요 시간 : 풀이 참조
'''

import sys


sys.stdin = open("input.txt", "r")
n = int(input())
n_mat = [list(map(int, input().split())) for _ in range(n)]

s = e = n // 2

res = 0

for i in range(n):
    for j in range(s, e+1):
        res += n_mat[i][j]
    if i < n // 2:
        s -= 1; e += 1
    else:
        s += 1; e -= 1

print(res)