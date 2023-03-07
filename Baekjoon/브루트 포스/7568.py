# 덩치
n = int(input())

students = list()
answer = list()

for i in range(n):
    w, h = map(int, input().split())
    students.append((w, h))

for i in students:
    rank = 1
    for j in students:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    answer.append(rank)

for i in answer:
    print(i, end=' ')