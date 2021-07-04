# 1. 런타임 에러
def solution(s):
    answer = []
    s = s.lower()
    strings = s.split(' ')
    for string in strings:
        if string[0].islower():
            string = string[0].upper() + string[1:].lower()
        answer.append(string)
    return " ".join(answer)

# 2. capitalize 내장함수 사용 시 런타임 에러 해결
def solution(s):
    answer = ''
    s = s.lower()
    strings = s.split(' ')
    for string in strings:
        answer += string.capitalize() + ' '
    return answer[:-1]