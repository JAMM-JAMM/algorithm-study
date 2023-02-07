'''
이분 검색
'''

'''
풀이 날짜 : 2023-02-04
풀이 시간 : 풀이 참조
'''

# import sys


# sys.stdin = open("input.txt", "r")
# n, m = map(int, input().split())
# lst = list(map(int, input().split()))

# lst.sort()

# lt = 0; rt = n-1

# while lt <= rt:
#     mid = (lt + rt) // 2
#     if lst[mid] == m:
#         print(mid + 1)
#         break
#     elif lst[mid] > m:
#         rt = mid - 1
#     else:
#         lt = mid + 1

'''
풀이 날짜 : 2023-02-07
풀이 시간 : 풀이 참조
'''

import sys


sys.stdin = open("input.txt", "r")
n, m = map(int, input().split())
n_lst = list(map(int, input().split()))

n_lst.sort()

lt = 0
rt = n - 1

while lt <= rt:
    mid = (lt + rt) // 2
    if n_lst[mid] == m:
        print(mid+1)
        break
    elif n_lst[mid] > m:
        rt = mid - 1
    else:
        lt = mid + 1