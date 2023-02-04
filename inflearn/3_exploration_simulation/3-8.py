'''
곳감(모래시계)
'''

'''
풀이 날짜 : 2023-02-01
풀이 소요 시간 : 풀이 참조
'''

# import sys


# sys.stdin = open("input.txt", "r")
# n = int(input())
# n_mat = [list(map(int, input().split())) for _ in range(n)]

# m = int(input())

# for i in range(m):
#     r, d, k = map(int, input().split())
#     if d == 0: # 왼쪽으로 이동
#         for _ in range(k):
#             n_mat[r-1].append(n_mat[r-1].pop(0))
#     else: # 오른쪽으로 이동
#         for _ in range(k):
#             n_mat[r-1].insert(0, n_mat[r-1].pop())

# res = 0
# s = 0; e = n-1

# for i in range(n):
#     for j in range(s, e+1):
#         res += n_mat[i][j]
#     if i < n // 2:
#         s += 1; e -= 1
#     else:
#         s -= 1; e += 1

# print(res)

'''
풀이 날짜: 2023-02-04
풀이 시간: 
'''

import sys


sys.stdin = open("input.txt", "r")
n = int(input())
n_mat = [list(map(int, input().split())) for _ in range(n)]
m = int(input())

for i in range(m):
    r, d, k = map(int, input().split())
    if d == 0:
        for _ in range(k):
            n_mat[r-1].append(n_mat[r-1].pop(0))
    else:
        for _ in range(k):
            n_mat[r-1].insert(0, n_mat[r-1].pop())

tot = 0

s = 0; e = n-1

for i in range(n):
    for j in range(s, e+1):
        tot += n_mat[i][j]
    if i < n // 2:
        s += 1; e -= 1
    else:
        s -= 1; e += 1

print(tot)