# 수 찾기

n = int(input())
n_nums = set(map(int, input().split()))
m = int(input())
m_nums = list(map(int, input().split()))

for num in m_nums:
    if num in n_nums:
        print(1)
    else:
        print(0)