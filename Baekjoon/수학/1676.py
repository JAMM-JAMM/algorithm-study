# 팩토리얼 0의 개수

n = int(input())

factorial = 1

count = 0

for i in range(1, n+1):
    factorial *= i

fact = str(factorial)

for j in range(len(fact)-1, -1, -1):
    if fact[j] != '0':
        print(count)
        break
    else:
        count += 1