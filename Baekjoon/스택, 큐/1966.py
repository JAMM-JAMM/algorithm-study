# 프린터 큐

from collections import deque

t = int(input())

answer = []

for _ in range(t):
    n, target = map(int, input().split())
    document_list = [i for i in range(n)]
    priority_list = list(map(int, input().split()))

    queue = deque([])

    for i in range(n):
        queue.append((document_list[i], priority_list[i]))
    
    count = 1
    result = []

    while queue:

        previous_length = len(queue)

        priority = queue.popleft()

        for j in range(len(queue)):
            if priority[1] < queue[j][1]:
                queue.append(priority)
                break
        
        after_length = len(queue)

        if previous_length != after_length:
            result.append(priority[0])
    
    for i in range(len(result)):
        if target == result[i]:
            answer.append(i+1)

for i in answer:
    print(i)
        



