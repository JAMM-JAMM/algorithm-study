# 파도반 수열

t = int(input())

test = []

for _ in range(t):
    test.append(int(input()))

p = [1, 1, 1, 2, 2]

for i in range(5, 100):
    p.append(p[i-5] + p[i-1])

for i in test:
    print(p[i-1])