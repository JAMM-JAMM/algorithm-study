'''
주사위 게임

풀이 날짜 : 2023-01-22
풀이 소요 시간 : 24분
'''

import sys
from collections import Counter


sys.stdin = open("input.txt", "r")

n = int(input())

result = 0

for i in range(n):
    nums = list(map(int, input().split()))
    if len(list(Counter(nums))) == 1:
        tmp = 10000 + (nums[0] * 1000)
        if tmp > result:
            result = tmp
    elif len(list(Counter(nums))) == 2:
        tmp = 1000 + (Counter(nums).most_common(1)[0][0] * 100)
        if tmp > result:
            result = tmp
    else:
        tmp = max(nums) * 10
else:
    print(result)