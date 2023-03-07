# 1, 2, 3 더하기

t = int(input())

nums = [int(input()) for _ in range(t)]

def dp(n):
    if n == 1:
        return 1
    
    if n == 2:
        return 2
    
    if n == 3:
        return 4
    
    return dp(n-1) + dp(n-2) + dp(n-3)

for num in nums:
    print(dp(num))