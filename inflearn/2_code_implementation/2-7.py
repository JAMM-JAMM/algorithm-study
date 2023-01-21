'''
소수 (에라토스테네스 체)

풀이 참고
'''

import sys


sys.stdin = open("input.txt")
n = int(input())

cnt = n - 1
for i in range(2, n+1):
