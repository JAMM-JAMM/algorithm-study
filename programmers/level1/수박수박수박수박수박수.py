def solution(n):
    if n % 2 == 0:
        answer = '수박' * int(n/2)
        return answer
    else:
        answer = '수박' * int((n-1)/2)
        return answer + '수'