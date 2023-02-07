'''
씨름 선수(그리디)
'''

'''
풀이 날짜 : 2023-02-07
'''

import sys


sys.stdin = open("input.txt", "r")
n = int(input())

n_lst = list()

for _ in range(n):
    h, w = map(int, input().split())
    n_lst.append((h, w))

n_lst.sort(reverse=True)

cnt = 0
largest = 0

for h, w in n_lst:
    if w > largest:
        largest = w
        cnt += 1

print(cnt)