# 덱


import sys
from collections import deque

n = int(sys.stdin.readline())

queue = deque([])

for _ in range(n):
    comm = sys.stdin.readline().rstrip().split()

    if comm[0] == 'push_front':
        queue.appendleft(comm[1])
    
    elif comm[0] == 'push_back':
        queue.append(comm[1])
    
    elif comm[0] == 'pop_front':
        if len(queue) != 0:
            print(queue.popleft())
        else:
            print(-1)
    
    elif comm[0] == 'pop_back':
        if len(queue) != 0:
            print(queue.pop())
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
