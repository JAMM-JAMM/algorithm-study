def solution(a, b):
    answer = 0
    if a > b:
        m = a
        n = b
    elif a < b:
        m = b
        n = a
    else:
        return a
    for i in range(n, m+1):
        answer += i
    return answer