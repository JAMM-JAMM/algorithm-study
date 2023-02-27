def solution(n, left, right):
    
    answer = list()
    
    for i in range(left, right+1):
        a = (i // n) + 1
        b = (i % n) + 1
        if a < b:
            a, b = b, a
        answer.append(a)
    return answer