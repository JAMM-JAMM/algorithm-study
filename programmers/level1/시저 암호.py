import string


def solution(s, n):
    answer = ''
    l = list(string.ascii_lowercase)
    u = list(string.ascii_uppercase)
    for i in s:
        if i in l:
            idx = l.index(i)
            try:
                answer += l[idx+n]
            except:
                answer += l[idx+n-len(l)]
        elif i in u:
            idx = u.index(i)
            try:
                answer += u[idx+n]
            except:
                answer += u[idx+n-len(u)]
        else:
            answer += ' '
    return answer