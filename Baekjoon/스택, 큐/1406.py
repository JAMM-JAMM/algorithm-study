# 에디터
# 정답은 맞지만...시간초과

import sys


s = list(sys.stdin.readline().rstrip())
m = int(input().rstrip())
command = []

for _ in range(m):
    command.append(sys.stdin.readline().rstrip())

cursor = len(s)

for comm in command:
    if comm == "L":
        if cursor != 0:
            cursor -= 1
    elif comm == "D":
        if cursor != len(s):
            cursor += 1
    elif comm == "B":
        if cursor != 0:
            s.pop(cursor-1)
            cursor -= 1
    else:
        temp = comm.split(' ')[-1]
        s.insert(cursor, temp)
        cursor += 1

print(s)
