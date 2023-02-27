def solution(s):
    stack = list()
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(s[i])
        else: # s[i] == ')'
            if not stack:
                return False
            else:
                stack.pop()
    if stack:
        return False
    return True