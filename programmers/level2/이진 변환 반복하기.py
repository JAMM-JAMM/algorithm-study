# 월간 코드 챌린지 시즌1

def solution(s):
    answer = []
    count = 0
    zero_count = 0
    while True:
        zero_count += s.count("0")
        one_count = s.count("1")
        temp = len("1" * one_count)
        s = format(temp, 'b')
        count += 1
        if s == "1":
            answer.append(count)
            answer.append(zero_count)
            break
    return answer