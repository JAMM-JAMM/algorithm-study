'''
회문 문자열 검사

풀이 날짜 : 2023-01-22
풀이 소요 시간 : 7분
'''

import sys


sys.stdin = open("input.txt", "r")
n = int(input())

for i in range(n):
    word = input().lower()
    reverse_word = word[::-1]
    if word == reverse_word:
        print("#{} YES".format(i+1))
    else:
        print("#{} NO".format(i+1))