'''
K번째 큰 수
'''

# import sys


# sys.stdin = open("input.txt", "r")
# n, k = map(int, input().split())
# nums = list(map(int, input().split()))

# sum_set = set() # 3개의 숫자의 합 중에서 중복되는 숫자가 없도록 하는 자료구조 - set()
# for i in range(n):
#     for j in range(i+1, n):
#         for l in range(j+1, n):
#             sum_set.add(nums[i] + nums[j] + nums[l])

# sum_lst = sorted(list(sum_set), reverse=True)
# print(sum_lst[k-1])

'''
2022-01-16
'''
import sys


sys.stdin = open("input.txt", "r")
n, k = map(int, input().split())
nums = list(map(int, input().split()))

sum_set = set()

for i in range(n):
    for j in range(i+1, n):
        for l in range(j+1, n):
            sum_set.add(nums[i] + nums[j] + nums[l])

sum_lst = sorted(list(sum_set), reverse=True)
print(sum_lst[k-1])