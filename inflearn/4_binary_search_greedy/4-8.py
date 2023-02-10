'''
침몰하는 타이타닉 (그리디)
'''

'''
풀이 날짜 : 2023-02-10
'''

import sys
from collections import deque


sys.stdin = open("input.txt", "r")
n, m = map(int, input().split())
p = list(map(int, input().split()))

p.sort()
# p = deque(p)

cnt = 0

while p:
    if len(p) == 1:
        cnt += 1
        break
    if p[0] + p[-1] > m:
        p.pop()
        cnt += 1
    else:
        p.pop()
        p.pop(0)
        # p.popleft()
        cnt += 1

print(cnt)

