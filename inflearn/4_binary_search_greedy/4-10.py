'''
역수열(그리디)
'''

'''
풀이 날짜 : 2023-02-10
'''

# import sys


# sys.stdin = open("input.txt", "r")
# n = int(input())
# lst = list(map(int, input().split())) # 4 8 6 2 5 1 3 7

# res = []

# for i in range(1, n+1):
#     cnt = 0
#     i_idx = lst.index(i)
#     for j_idx, j in enumerate(lst):
#         if (j_idx < i_idx) and (j > i):
#             cnt += 1
#     res.append(cnt)

# print(res)

import sys


sys.stdin = open("input.txt", "r")
n = int(input())
lst = list(map(int, input().split()))

chk_lst = [0] * n 

for i in range(n):
    for j in range(n):
        if (lst[i] == 0 and chk_lst[j] == 0):
            chk_lst[j] = i + 1
            break
        elif chk_lst[j] == 0:
            lst[i] -= 1
        print("{}, {} : {}".format(i, j, lst))
    print("{} : {}".format(i, chk_lst))

print(chk_lst)