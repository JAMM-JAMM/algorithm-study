# 비밀번호 찾기

n, m = map(int, input().split())

hsh = dict()

for _ in range(n):
    memo = input().split()
    hsh[memo[0]] = memo[1]

for _ in range(m):
    site = input()
    print(hsh[site])