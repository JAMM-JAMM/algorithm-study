'''
증가수열 만들기(그리디)
'''

'''
풀이 날짜 : 2023-02-10
'''

import sys


sys.stdin = open("input.txt", "r")
n = int(input())
n_lst = list(map(int, input().split()))

lt = 0
rt = n - 1
last = 0
res = ''
tmp = []

while lt <= rt:
    if n_lst[lt] > last:
        tmp.append((n_lst[lt], 'L'))
    if n_lst[rt] > last:
        tmp.append((n_lst[rt], 'R'))
    
    tmp.sort()

    if len(tmp) == 0:
        break
    else:
        res += tmp[0][1]
        last = tmp[0][0]
        if tmp[0][1] == 'L':
            lt += 1
        else:
            rt -= 1
    
    tmp.clear()

print(len(res))
print(res)