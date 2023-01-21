'''
점수계산

풀이 날짜 : 2023-01-22
풀이 소요 시간 : 11분
'''

import sys


sys.stdin = open("input.txt", "r")
n = int(input())
check_list = list(map(int, input().split()))
score_list = [0] * n

for i, check in enumerate(check_list):
    if i == 0:
        if check_list[i] == 1:
            score_list[i] = 1
    else:
        if check_list[i] == 1:
            if check_list[i-1] == 0:
                score_list[i] = 1
            else:
                score_list[i] = score_list[i-1] + 1

print(sum(score_list))