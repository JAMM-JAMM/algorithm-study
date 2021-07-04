def solution(s):
    answer = ''
    temp = s.split(' ')
    for i in range(len(temp)):
        for j in range(len(temp[i])):
            if (j == 0) or (j % 2 == 0):
                answer += temp[i][j].upper()
            elif j % 2 == 1:
                answer += temp[i][j].lower()
        if i != len(temp)-1:
            answer += ' '
    return answer