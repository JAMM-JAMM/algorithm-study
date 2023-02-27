def solution(s):
    stack = []
    for x in s:
        if not stack:
            stack.append(x)
        elif x == stack[-1]:
            stack.pop()
        else:
            stack.append(x)
    if stack:
        return 0
    else:
        return 1