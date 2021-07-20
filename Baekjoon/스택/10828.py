# 스택

n = int(input())
command = []

stack = []

for _ in range(n):
    command.append(input())

for comm in command:
    if comm == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif comm == 'size':
        print(len(stack))
    elif comm == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif comm == 'top':
        if len(stack) != 0:
            print(stack[-1])
        else:
            print(-1)
    else:
        stack.append(comm.split(' ')[1])