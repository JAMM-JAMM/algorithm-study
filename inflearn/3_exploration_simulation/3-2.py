'''
숫자만 추출

풀이 날짜 : 2023-01-22
풀이 소요 시간 : 11분
'''

import sys


sys.stdin = open("input.txt", "r")
word = input()

num = ''
div_cnt = 0

for w in word:
    if w.isdecimal():
        num += w
else:
    num = int(num)
    for i in range(1, num+1):
        if num % i == 0:
            div_cnt += 1

print(num)
print(div_cnt)