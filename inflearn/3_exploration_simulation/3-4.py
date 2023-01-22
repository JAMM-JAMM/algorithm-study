'''
두 리스트 합치기

풀이 날짜 : 2023-01-22
풀이 소요 시간 : 7분
'''

import sys

sys.stdin = open("input.txt", "r")
n = int(input())
n_lst = list(map(int, input().split()))
m = int(input())
m_lst = list(map(int, input().split()))

lst = sorted(n_lst + m_lst)
for x in lst:
    print(x, end=' ')