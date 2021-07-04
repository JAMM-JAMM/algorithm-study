def solution(n):
    answer = 0
    n_one_count = format(n, 'b').count('1')
    while True:
        n += 1
        temp_one_count = format(n, 'b').count('1')
        if n_one_count == temp_one_count:
            return n