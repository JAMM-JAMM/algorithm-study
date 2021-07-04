def solution(n):
    answer = 0
    for i in range(1, n+1):
        s = 0
        while True:
            if s == n:
                answer += 1
                break
            elif s > n:
                break
            s += i
            i += 1
    return answer