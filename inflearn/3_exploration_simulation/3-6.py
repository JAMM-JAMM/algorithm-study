'''
격자판 최대합
'''

'''
풀이 날짜 : 2023-02-01
풀이 소요 시간 : 25분
'''

# import sys


# sys.stdin = open("input.txt", "r")
# n = int(input())
# n_mat = [list(map(int, input().split())) for _ in range(n)]

# sums = []

# for i in range(n):
#     # 각 행의 합
#     sums.append(sum(n_mat[i]))
    
#     # 각 열의 합
#     col_sum = 0
#     for j in range(n):
#         col_sum += n_mat[j][i]
#     sums.append(col_sum)

# # 대각선의 합
# ax_sum_1 = 0
# ax_sum_2 = 0
# for i in range(n):
#     ax_sum_1 += n_mat[i][i]
#     ax_sum_2 += n_mat[i][n-i-1]

# sums.append(ax_sum_1)
# sums.append(ax_sum_2)

# print(max(sums))

# import sys


# sys.stdin = open("input.txt", "r")
# n = int(input())
# n_mat = [list(map(int, input().split())) for _ in range(n)]

# largest = -2147000000

# for i in range(n):
#     sum1=sum2=0
#     for j in range(n):
#         sum1 += n_mat[i][j] # 각 행의 합
#         sum2 += n_mat[j][i] # 각 열의 합
#     if sum1 > largest:
#         largest = sum1
#     if sum2 > largest:
#         largest = sum2

# sum1=sum2=0
# for i in range(n):
#     sum1 = n_mat[i][i]
#     sum2 = n_mat[i][n-i-1]
# if sum1 > largest:
#     largest = sum1
# if sum2 > largest:
#     largest = sum2

# print(largest)

'''
풀이 날짜 : 2023-02-04
풀이 시간 : 10분
'''

import sys


sys.stdin = open("input.txt", "r")
n = int(input())
n_mat = [list(map(int, input().split())) for _ in range(n)]

largest = -2147000000

for i in range(n):
    row_sum = 0; col_sum = 0
    for j in range(n):
        row_sum += n_mat[i][j] # 각 행의 합
        col_sum += n_mat[j][i] # 각 열의 합
    if row_sum > largest:
        largest = row_sum
    if col_sum > largest:
        largest = col_sum

a_axis_sum = 0; b_axis_sum = 0
for i in range(n):
    a_axis_sum += n_mat[i][i]
    b_axis_sum += n_mat[i][n-i-1]
if a_axis_sum > largest:
    largest = a_axis_sum
if b_axis_sum > largest:
    largest = b_axis_sum

print(largest)