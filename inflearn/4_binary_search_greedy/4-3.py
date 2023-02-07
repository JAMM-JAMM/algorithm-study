'''
이분 검색
'''

'''
풀이 날짜 : 2023-02-07
풀이 시간 : 풀이 참조
'''

import sys


sys.stdin = open("input.txt", "r")
n, m = map(int, input().split()) # n: 곡의 개수, m: DVD 개수
n_lst = list(map(int, input().split()))

res = 0 # DVD의 최소 용량 크기
lt = 1 # DVD의 최소 용량 크기를 정하기 위한 최소 구간 값
rt = sum(n_lst) # DVD의 최대 용량 크기를 정하기 위한 최대 구간 값
n_max = max(n_lst) # DVD의 최소 용량 크기는 곡 중 가장 큰 곡의 용량의 크기보다 크거나 같아야 한다.

def Counter(capacity):
    cnt = 1
    summ = 0
    for x in n_lst:
        if summ + x > capacity:
            summ = x
            cnt += 1
        else:
            summ += x
    return cnt


while lt <= rt:
    mid = (lt + rt) // 2
    if mid >= n_max and Counter(mid) <= m:
        res = mid
        rt = mid - 1
    else:
        lt = mid + 1

print(res)