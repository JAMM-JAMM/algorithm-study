def solution(phone_number):
    answer = ''
    l = len(phone_number)
    for i in range(l-4):
        answer += '*'
    for j in range(l-4, l):
        answer += phone_number[j]
    return answer