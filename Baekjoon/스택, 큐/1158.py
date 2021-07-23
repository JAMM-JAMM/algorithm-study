# 요세푸스 순열


n, k = map(int, input().split())

stack = [i+1 for i in range(n)]

temp = k-1

count = 0

result = []

while stack:
    count = (count + temp) % len(stack)
    result.append(stack[count])
    stack.pop(count)

print("<%s>" % (', '.join(map(str, result))))