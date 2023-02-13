'''
쇠막대기
'''

'''
풀이 날짜 : 2023-02-13
'''

import sys


sys.stdin = open("input.txt", "r")
lst = input()

stack = []
cnt = 0

for i in range(len(lst)):
    if lst[i] == '(':
        stack.append(lst[i])
    else: # lst[i] == ')'
        if lst[i-1] == '(':
            stack.pop()
            cnt += len(stack)
        else:
            stack.pop()
            cnt += 1

print(cnt)