'''
교육 과정 설계(큐)
'''

'''
풀이 날짜 : 2023-02-24
'''

import sys
from collections import deque


sys.stdin = open("input.txt", "r")
needs = input()
n = int(input())

for i in range(n):
    plan = input()
    dq = deque(needs)
    for x in plan:
        if x in dq:
            if x != dq.popleft():
                print("#{} NO".format(i+1))
                break
    else:
        if len(dq) == 0:
            print("#{} YES".format(i+1))
        else:
            print("#{} NO".format(i+1))
