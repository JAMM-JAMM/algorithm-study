def solution(x):
    temp = str(x)
    x_sum = 0
    for i in temp:
        x_sum += int(i)
    if x % x_sum == 0:
        return True
    elif x % x_sum != 0:
        return False