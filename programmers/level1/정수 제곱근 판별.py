from math import sqrt

def solution(n):
    sqrt_n = sqrt(n)
    if sqrt_n - int(sqrt_n) == 0:
        return (sqrt_n + 1) ** 2
    else:
        return -1