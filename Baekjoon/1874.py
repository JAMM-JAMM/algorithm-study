# 스택 수열

n = int(input())

stack = []
result = []
count = 0
msg = True

for _ in range(n):
    element = int(input())

    while count < element:
        count += 1
        stack.append(count)
        result.append("+")

    if stack[-1] == element:
        stack.pop()
        result.append('-')
    else:
        msg = False
        break

if msg == False:
    print("NO")
else:
    print("\n".join(result))
        
