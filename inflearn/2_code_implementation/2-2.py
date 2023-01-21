'''
K번째 수
'''

# # 나의 풀이

# import sys


# sys.stdin = open("input.txt", "rt")

# T = int(input())
# for t in range(T):
#     n, s, e, k = map(int, input().split())
#     nums = list(map(int, input().split()))
    
#     n_nums = sorted(nums[s-1:e])
#     print(n_nums[k-1])

# # 다른 풀이

# import sys
# sys.stdin=open("input.txt", "r")
# T=int(input())
# for t in range(T):
#     n, s, e, k=map(int, input().split())
#     a=list(map(int, input().split()))
#     a=a[s-1:e]
#     a.sort()
#     print("#%d %d" %(t+1, a[k-1]))

'''
2022-01-16 (월)
'''

import sys


sys.stdin = open("input.txt", "r")
T = int(input())

for t in range(T):
    n, s, e, k = map(int, input().split())
    nums = list(map(int, input().split()))
    n_nums = sorted(nums[s-1:e])
    print("#{} {}".format(t+1, n_nums[k-1]))