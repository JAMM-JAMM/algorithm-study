# 괄호

t = int(input())
pss = []

for _ in range(t):
    pss.append(input())

for ps in pss:
    stack = []
    flag = 0
    for i in ps:
        if i == '(':
            stack.append(i)
        else:
            if len(stack) != 0:
                stack.pop()
            else:
                print("NO")
                flag = 1
                break
    if len(stack) == 0 and flag == 0:
        print("YES")
    elif len(stack) != 0 and flag == 0:
        print("NO")
