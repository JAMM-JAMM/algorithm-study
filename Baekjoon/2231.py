# 분해합

n = int(input())

for i in range(1, n+1):
    n_list = list(map(int, str(i)))
    answer = i + sum(n_list)
    if answer == n:
        print(i)
        break
    if i == n:
        print(0)

