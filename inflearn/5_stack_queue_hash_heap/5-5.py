'''
공주 구하기 (큐)
'''

'''
풀이 날짜 : 2023-02-24
'''

import sys
from collections import deque


sys.stdin = open("input.txt", "r")
n, k = map(int, input().split())

dq = list(range(1, n+1))
dq = deque(dq)

while dq:
    for _ in range(k-1):
        dq.append(dq.popleft())
    dq.popleft()
    if len(dq) == 1:
        print(dq[0])
        dq.popleft()