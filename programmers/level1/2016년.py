def solution(a, b):
    day = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    answer = {0:'THU', 1:'FRI', 2:'SAT', 3:'SUN', 4:'MON', 5:'TUE', 6:'WED'}
    tot = 0
    for i in range(1, a):
        tot += day[i]
    tot += b
    weekday = answer[tot % 7]
    return weekday