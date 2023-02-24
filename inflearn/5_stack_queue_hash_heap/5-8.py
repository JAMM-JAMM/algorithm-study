'''
단어 찾기(해쉬)
'''

'''
풀이 날짜 : 2023-02-24
'''

import sys


sys.stdin = open("input.txt", "r")
n = int(input())
word_dict = dict()
for i in range(n):
    word = input()
    word_dict[word] = 1
for i in range(n-1):
    word = input()
    word_dict[word] = 0
for key, val in word_dict.items():
    if val == 1:
        print(key)