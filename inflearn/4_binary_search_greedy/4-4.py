'''
마구간 정하기 (결정 알고리즘)
'''

'''
풀이 날짜 : 2023-02-07
'''

import sys


sys.stdin = open("input.txt", "r")
n, c = map(int, input().split())

n_lst = list()
for _ in range(n):
    tmp = int(input())
    n_lst.append(tmp)

n_lst.sort()

lt = 1
rt = n_lst[n-1]
res = 0

def Counter(length):
    cnt = 1
    ep = n_lst[0]
    for i in range(1, n):
        if n_lst[i] - ep >= length:
            cnt += 1
            ep = n_lst[i]
    return cnt

while lt <= rt:
    mid = (lt + rt) // 2
    if Counter(mid) >= c:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(res)