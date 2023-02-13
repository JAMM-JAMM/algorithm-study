'''
가장 큰 수
'''

'''
풀이 날짜 : 2023-02-13
'''

import sys


sys.stdin = open("input.txt", "r")
n, m = map(int, input().split())
nums = list(map(int, str(n)))

stack = []

for n in nums:
    while stack and m > 0 and stack[-1] < n:
        stack.pop()
        m -= 1
    stack.append(n)
if m != 0:
    stack = stack[:-m]

print(stack)