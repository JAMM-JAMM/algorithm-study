# 나는야 포켓몬 마스터 이다솜

import sys


n, m = map(int, sys.stdin.readline().split())

book_name = dict()
book_number = dict()

for i in range(n):
    poketmon = sys.stdin.readline().strip()
    book_number[i+1] = poketmon
    book_name[poketmon] = i+1

for _ in range(m):
    problem = sys.stdin.readline().strip()

    try:
        print(book_name[problem])
    except:
        print(book_number[int(problem)])

