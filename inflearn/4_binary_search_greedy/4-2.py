'''
랜선자르기(결정알고리즘)
'''

'''
풀이날짜 : 2023-02-04
'''

# import sys


# sys.stdin = open("input.txt", "r")
# k, n = map(int, input().split())

# largest = 0
# lst = []
# for _ in range(k):
#     tmp = int(input())
#     lst.append(tmp)
#     largest = max(tmp, largest)

# def Count(len):
#     cnt = 0
#     for x in lst:
#         cnt += (x // len)
#     return cnt

# lt = 1
# rt = largest
# res = 0
# while lt <= rt:
#     mid = (lt + rt) // 2
#     if Count(mid) >= n:
#         res = mid
#         lt = mid + 1
#     else:
#         rt = mid - 1
#     # print("lt = {}, rt = {}, mid = {}, res = {}, count = {}".format(lt, rt, mid, res, Count(mid)))


# print(res)

'''
풀이 날짜 : 2023-02-07
'''

import sys


sys.stdin = open("input.txt", "r")
k, n = map(int, input().split())

lst = list()
largest = 0

for _ in range(k):
    tmp = int(input())
    lst.append(tmp)
    largest = max(largest, tmp)

lt = 1 # 랜선을 만들 수 있는 최소 구간의 초기 값
rt = largest # 랜선을 만들 수 있는 최대 구간의 초기 값
res = 0 # N개를 만들 수 있는 랜선의 최대 길이

def Counter(length):
    cnt = 0
    for x in lst:
        cnt += (x // length)
    return cnt

while lt <= rt:
    mid = (lt + rt) // 2
    if Counter(mid) >= n:
        lt = mid + 1
        res = mid
    else:
        rt = mid - 1

print(res)