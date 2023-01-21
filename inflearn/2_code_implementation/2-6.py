'''
자릿수의 합

풀이 날짜 : 2023-01-21
풀이 소요 시간 : 31분
'''

import sys


sys.stdin = open("input.txt")
n = int(input())
m = list(map(int, input().split()))

def digit_sum(x: int) -> int:
    sum_digit = 0
    for s in str(x):
        sum_digit += int(s)
    return sum_digit

result = dict()

for num, sum_digit in zip(m, list(digit_sum(s) for s in m)):
    result[str(num)] = sum_digit
else:
    print(list(int(k) for k, v in result.items() if max(result.values()) == v)[0])