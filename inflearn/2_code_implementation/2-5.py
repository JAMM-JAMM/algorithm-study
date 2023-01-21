'''
정다면체

풀이 날짜 : 2023-01-21
풀이 소요 시간 : 13분
'''

import sys


sys.stdin = open("input.txt")
n, m = map(int, input().split())

sum_count = dict()

for i in range(1, n+1):
    for j in range(1, m+1):
        if str(i+j) not in sum_count:
            sum_count[str(i+j)] = 1
        else:
            sum_count[str(i+j)] += 1

print(*sorted([int(k) for k, v in sum_count.items() if max(sum_count.values()) == v]))