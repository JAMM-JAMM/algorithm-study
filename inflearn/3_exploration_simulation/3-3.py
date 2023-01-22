'''
카드 역배치

풀이 날짜 : 2023-01-22
풀이 소요 시간 : 13분
'''

import sys


sys.stdin = open("input.txt")

org = [x for x in range(21)]

for i in range(10):
    a, b = map(int, input().split())
    front_lst = org[:a]; mid_lst = org[a:b+1]; end_lst = org[b+1:]
    org = front_lst + mid_lst[::-1] + end_lst
print(org)