'''
회의실 배정(그리디)
'''

'''
풀이 날짜 : 2023-02-07
'''

import sys


sys.stdin = open("input.txt", "r")
n = int(input())
n_lst = list()

for _ in range(n):
    s, e = map(int, input().split())
    n_lst.append((s, e))

n_lst.sort(key=lambda x: (x[1], x[0]))

cnt = 0
ep = 0

for s, e in n_lst:
    if s >= ep:
        cnt += 1
        ep = e

print(cnt)