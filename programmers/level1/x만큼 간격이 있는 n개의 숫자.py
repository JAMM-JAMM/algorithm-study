def solution(x, n):
    result = []
    for i in range(n):
        result.append(x + (x * i))
    return result