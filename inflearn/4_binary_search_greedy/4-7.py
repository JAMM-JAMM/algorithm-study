'''
창고 정리
'''

'''
풀이 날짜 : 2023-02-08
'''

import sys


sys.stdin = open("input.txt", "r")
l = int(input())
l_lst = list(map(int, input().split()))
m = int(input())

l_lst.sort()

for _ in range(m):
    l_lst[0] += 1
    l_lst[l-1] -= 1
    l_lst.sort()

print(l_lst[l-1] - l_lst[0])