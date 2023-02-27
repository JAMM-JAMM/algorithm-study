def solution(n):
    f_list = [0, 1]
    for i in range(2, n+1):
        tmp = f_list[-1] + f_list[-2]
        f_list.append(tmp)
    answer = f_list[-1] % 1234567
    return answer