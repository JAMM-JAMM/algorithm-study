# 듣보잡

n, m = map(int, input().split())

n_list = set()
m_list = set()

for _ in range(n):
    n_list.add(input())

for _ in range(m):
    m_list.add(input())

answer = list(n_list & m_list)
answer.sort()

print(len(answer))

for i in range(len(answer)):
    print(answer[i])