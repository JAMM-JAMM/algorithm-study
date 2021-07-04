def solution(num):
    if num == 1:
        return 0
    for i in range(500):
        if num % 2 == 0:
            num = num / 2
            if num == 1:
                return i+1
        else:
            num = 1 + (num * 3)
            if num == 1:
                return i+1
    return -1