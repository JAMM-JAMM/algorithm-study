def solution(n):
    n_bin = bin(n)[2:]
    n_bin_one_cnt = n_bin.count('1')
    while True:
        n += 1
        tmp_bin = bin(n)[2:]
        tmp_bin_one_cnt = tmp_bin.count('1')
        if n_bin_one_cnt == tmp_bin_one_cnt:
            return n