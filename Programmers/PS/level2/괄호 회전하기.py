from collections import deque

def solution(s):
    cnt = 0
    l = len(s)
    dq = deque(s)
    
    for i in range(l):
        
        if i != 0:
            dq.append(dq.popleft())
        
        stack = list()
        
        for q in dq:
            if stack:
                if stack[-1] == '[' and q == ']':
                    stack.pop()
                elif stack[-1] == '(' and q == ')':
                    stack.pop()
                elif stack[-1] == '{' and q == '}':
                    stack.pop()
                else:
                    stack.append(q)
            else:
                stack.append(q)
                
        if not stack:
            cnt += 1
    
    return cnt