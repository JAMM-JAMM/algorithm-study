'''
스도쿠 검사
풀이 날짜 : 2023-02-04
풀이 시간 : 풀이 참조
'''

import sys


sys.stdin = open("input.txt", "r")
n_mat = [list(map(int, input().split())) for _ in range(9)]

def sudoku(mat):
    for i in range(9):
        ch_row = [0] * 10
        ch_col = [0] * 10
        for j in range(9):
            ch_row[n_mat[i][j]] = 1
            ch_col[n_mat[j][i]] = 1
        if sum(ch_row) != 9 or sum(ch_col) != 9:
            return False
    for i in range(3):
        for j in range(3):
            ch_rec = [0] * 10
            for k in range(3):
                for s in range(3):
                    ch_rec[n_mat[i*3+k][j*3+k]] = 1
            if sum(ch_rec) != 9:
                return False
    return True

if sudoku(n_mat):
    print("YES")
else:
    print("NO")