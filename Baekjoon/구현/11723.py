# 집합

import sys


m = int(sys.stdin.readline())

answer = set()

for _ in range(m):
    command = sys.stdin.readline().strip().split()

    if len(command) == 1:
        if command[0] == "all":
            answer = set([i+1 for i in range(20)])
        else:
            answer = set()
    
    else:
        op, num = command[0], int(command[1])

        if op == "add":
            answer.add(num)
        elif op == "remove":
            answer.discard(num)
        elif op == "check":
            if num in answer:
                print(1)
            else:
                print(0)
        elif op == "toggle":
            if num in answer:
                answer.discard(num)
            else:
                answer.add(num)
