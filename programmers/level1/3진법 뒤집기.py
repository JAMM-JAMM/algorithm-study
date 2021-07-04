# 월간 코드 챌린지 시즌2

def solution(n):
    answer = ''
    result = 0
    
    while True:
        q, r = divmod(n, 3)
        n = q
        answer += str(r)
        if q == 0:
            break
    
    idx = 0
    for i in range(len(answer)-1, -1, -1):
        result += int(answer[i]) * (3 ** idx)
        idx += 1
    
    return result