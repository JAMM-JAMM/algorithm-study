'''
뒤집은 소수

풀이 날짜 : 2023-01-22
풀이 소요 시간 : 16분
'''

import sys


sys.stdin = open("input.txt", "r")
n = int(input())
nums = list(map(int, input().split()))

def reverse(x: int) -> int:
    return int(str(x)[::-1])

def isPrime(x: int) -> bool:
    for i in range(2, x):
        if x % i == 0:
            return False
    else:
        return True

for num in nums:
    reverse_num = reverse(num)
    if isPrime(reverse_num):
        print(reverse_num, end=' ')