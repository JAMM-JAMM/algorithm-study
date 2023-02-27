def solution(brown, yellow):
    a = brown + yellow
    for i in range(1, a+1):
        if a % i == 0:
            b = a // i
            if b >= i:
                if (b - 2) * (i - 2) == yellow:
                    return [b, i]
        