# 1로 만들기

# 1: 1
# 2: 2 - 1
# 3: 3 - 1
# 4: 4 - 2 - 1
# 5: 5 - 4 - 2 - 1
# 6: 6 - 2 - 1
# 7: 7 - 6 - 2 - 1
# 8: 8 - 4 - 2 - 1
# 9: 9 - 3 - 1
# 10: 10 - 9 - 3 - 1
# 11: 11 - 10 - 9 - 3 - 1
# 12: 12 - 6 - 2 - 1
# 13: 13 - 12 - 6 - 2 - 1
# 14: 14 - 7 - 6 - 2 - 1

n = int(input())

dp = [0 for i in range(n+1)]

for  i in range(2, n+1):
    dp[i] = dp[i-1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i//2]+1, dp[i])
    if i % 3 == 0:
        dp[i] = min(dp[i//3]+1, dp[i])

print(dp[-1])