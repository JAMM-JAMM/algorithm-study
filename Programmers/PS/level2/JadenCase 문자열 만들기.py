def solution(s):
    answer = ''
    word_list = s.split(' ')
    for word in word_list:
        answer += word.capitalize() + ' '
    return answer[:-1]