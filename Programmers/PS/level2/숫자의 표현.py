def solution(n):
    cnt = 0
    for i in range(1, n+1): # 시작 숫자
        tmp = 0
        for j in range(i, n+1):
            tmp += j
            if tmp > n:
                break
            if tmp == n:
                cnt += 1
                break
    return cnt