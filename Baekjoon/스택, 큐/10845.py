# 큐

import sys


n = int(sys.stdin.readline().rstrip())

queue = []

for _ in range(n):
    comm = sys.stdin.readline().rstrip().split()

    if comm[0] == 'push':
        queue.append(comm[1])
    
    elif comm[0] == 'pop':
        if len(queue) != 0:
            print(queue.pop(0))
        else:
            print(-1)
    
    elif comm[0] == 'size':
        print(len(queue))

    elif comm[0] == 'empty':
        if len(queue) != 0:
            print(0)
        else:
            print(1)
    
    elif comm[0] == 'front':
        if len(queue) != 0:
            print(queue[0])
        else:
            print(-1)
    
    elif comm[0] == 'back':
        if len(queue) != 0:
            print(queue[-1])
        else:
            print(-1)
    


