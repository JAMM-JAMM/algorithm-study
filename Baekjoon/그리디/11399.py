# ATM

n = int(input())

nums = list(map(int, input().split()))

nums.sort()

answer = 0

for i in range(n+1):
    answer += sum(nums[:i])

print(answer)