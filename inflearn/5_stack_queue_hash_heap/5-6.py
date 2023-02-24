'''
응급실 (큐)
'''

'''
풀이 날짜 : 2023-02-24
'''

import sys
from collections import deque


sys.stdin = open("input.txt", "r")
n, m = map(int, input().split())
lst = [(pos, val) for pos, val in enumerate(list(map(int, input().split())))]
dq = deque(lst)

cnt = 0

while True:
    cur = dq.popleft()
    if any(cur[1] < x[1] for x in dq):
        dq.append(cur)
    else:
        cnt += 1
        if cur[0] == m:
            print(cnt)
            break