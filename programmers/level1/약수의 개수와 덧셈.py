# 월간 코드 챌린지 시즌2

def solution(left, right):
    num = [i for i in range(left,right+1)]
    answer = 0
    for n in num:
        cnt = 0
        for i in range(1, n+1):
            if n % i == 0:
                cnt += 1
        if cnt % 2 == 0:
            answer += n
        else:
            answer -= n
    return answer