from collections import deque


def solution(priorities, location):
    answer = 0
    queue = deque([i for i in range(len(priorities))])
    doc_priority = {}
    for i in range(len(priorities)):
        doc_priority[i] = priorities[i]
    doc_priority_val = [v for k,v in doc_priority.items()]
    while len(queue) != 0:
        temp = queue.popleft()
        if doc_priority[temp] == max(doc_priority_val):
            del doc_priority_val[doc_priority_val.index(max(doc_priority_val))]
            answer += 1
            if temp == location:
                break
        else:
            queue.append(temp)
    return answer