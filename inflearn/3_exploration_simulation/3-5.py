'''
수들의 합

풀이 날짜 : 2023-01-22
풀이 소요 시간 : 8분
'''

import sys

sys.stdin = open("input.txt", "r")
n, m = map(int, input().split())
nums = list(map(int, input().split()))

cnt = 0

for i in range(n+1):
    for j in range(i+1, n+1):
        if sum(nums[i:j]) == m:
            cnt += 1

print(cnt)