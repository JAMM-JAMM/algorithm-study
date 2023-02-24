'''
재귀함수를 이용한 이진수 출력
'''

'''
풀이 날짜 : 2023-02-24
'''

import sys


sys.stdin = open("input.txt", "r")

def DFS(x):
    if x == 0:
        return
    else:
        DFS(x//2)
        print(x%2, end='')
        
n = int(input())
DFS(n)
    