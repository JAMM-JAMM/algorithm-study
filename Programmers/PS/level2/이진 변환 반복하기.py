def func(x):
    zero_cnt = x.count('0')
    x = x.replace('0', '')
    x_bin = bin(len(x))[2:]
    return zero_cnt, x_bin

def solution(s):
    cnt = 0
    zero_cnt = 0
    while True:
        a, s = func(s)
        zero_cnt += a
        cnt += 1
        if s == '1':
            break
    return [cnt, zero_cnt]
            